import random
import sys
import os
from os import system, name
#system('pip install pyenchant')
import enchant

class WordSet():


    def __init__(self):
        self.words = [["a","g","e","t"],
                      ["e","a","c","r","k"],
                      ["t","f","o"],
                      ["i","g","t","a"],
                      ["b","d","l","h","u","a"],
                      ["n","d","e","l","i","a"],
                      ["d","a","n","k","e"],
                      ["d","o","x","n","u","t"],
                      ["s","m","w","a"],
                      ["u","q","i","t","l"]]
        self.position = [(0,0)]
        self.button = [(0,0)]
        self.attempts = []
        self.guess = ""
        self.find = 3
        self.found = 0
        self.level = 0
        self.advancement = 0
        self.dictionary = enchant.Dict("en_us")

    def GetLetter(self,y):
        c=0
        for x in self.position:
            if ((x[0] > y[0]-15 and x[0] < y[0]+15) and (x[1] > y[1]-10 and x[1] < y[1]+10)):
                self.guess+=self.words[self.level][c-1]
                #self.guess = self.guess.rstrip()
                #print(5)
                #print (self.guess)
                return self.words[self.level][c-1]
            c= c+1
        return False

    def CheckButton(self,y):
        if ((self.button[0] > y[0]-50 and self.button[0] < y[0]+50) and (self.button[1] > y[1]-10 and self.button[1] < y[1]+10)):
            return True
        return False

    def CheckReal(self):

        if self.guess == "":
            return False

        for x in self.guess:
            passes = False
            for y in self.words[self.level]:
                if x == y:
                    passes = True
            if passes == False:
                self.guess = ""
                return False

        for x in self.attempts:
            if self.guess == x:
                self.guess = ""
                return False

        if self.dictionary.check(self.guess) and len(self.guess)>=3:
            self.attempts.append(self.guess)
            self.found = self.found + 1
            self.guess = ""
            return True
        self.guess = ""
        return False

    def Advance(self):
        self.attempts.clear()
        self.level = self.level+1
        self.advancement = self.advancement+1
        self.found = 0
        if self.advancement >= 9:
            self.find = self.find+1
            self.advancement = 0
            endGame = "yes"
            return endGame

    def GetString(self,index):
        TheString=""
        for x in self.words[index]:
            TheString += x + ", "
        TheString = TheString.rstrip(" ,")
        print(self.words[index])
        return TheString






'''
    books= WordSet()
    _ = system('cls')
    while books.level < len(books.words):
        while books.found < books.find:
            print("Level:", books.level+1)
            print("Words Found")
            for x in books.attempts:
                print(x, end =" ")  #end thing takes out newline
            print("")
            print("Found - ", books.found)
            print (books.words[books.level])
            books.guess = input("input word: ").lower()

            if WordSet.CheckReal(books):
                system('cls')
                print("you found a word!")
            else:
                system('cls')

        system('cls')
        print("Level Completed!")
        WordSet.Advance(books)


print("You have finished the game")
system('pip uninstall pyenchant')
'''
