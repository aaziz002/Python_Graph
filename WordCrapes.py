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

        return True



dictionary = enchant.Dict("en_us")


books= WordSet()
_ = system('cls')
while books.level < len(books.words):
    while books.found < books.find:
        print("Level:", books.level+1)
        print("Words Found")
        for x in books.attempts:
            print(x, end =" ")
        print("")
        print("Found - ", books.found)
        print (books.words[books.level])
        books.guess = input("input word: ").lower()

        if WordSet.CheckReal(books) and len(books.guess)>=3 and dictionary.check(books.guess):
            system('cls')
            books.attempts.append(books.guess)
            print("you found a word!")
            books.found = books.found + 1
        else:
            system('cls')

    system('cls')
    print("Level Completed!")
    books.attempts.clear()
    books.level = books.level+1
    books.advancement = books.advancement+1
    books.found = 0
    if books.advancement >= 9:
        books.find = books.find+1
        books.advancement = 0


print("You have finished the game")
'''system('pip uninstall pyenchant')'''
