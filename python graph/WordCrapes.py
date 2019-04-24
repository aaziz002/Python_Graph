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
        self.attempts = []
        self.guess = "Rabbit"
        self.find = 3
        self.found = 0
        self.level = 0
        self.advancement = 0
        self.dictionary = enchant.Dict("en_us")

    def CheckReal(self):

        for x in self.guess:
            passes = False
            for y in self.words[self.level]:
                if x == y:
                    passes = True
            if passes == False:
                return False

        for x in self.attempts:
            if self.guess == x:
              return False

        if self.dictionary.check(self.guess) and len(self.guess)>=3:
            self.attempts.append(self.guess)
            self.found = self.found + 1
            return True

        return False

    def Advance(self):
        self.attempts.clear()
        self.level = self.level+1
        self.advancement = self.advancement+1
        self.found = 0
        if self.advancement >= 9:
            self.find = self.find+1
            self.advancement = 0

    def GetString(self,index):
        TheString=""
        for x in self.words[index]:
            TheString += x + ", "
        TheString = TheString.rstrip(" ,")
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
