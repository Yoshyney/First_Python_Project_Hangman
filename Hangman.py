#!/usr/bin/env python3

#First Program in Python !

import time
import random
import os
clear = lambda: os.system('clear')


def drawing():
    print("---")
    print("|  |")
    print("|  o")
    print("| /|\ ")
    print("|  |") 
    print("| /-\ ")  
    print("---        Welcome To The Hangman !")

def chooseName():
    name = ""
    while name == "":
        name = input("What is your name? ")
        if(name == ""):
            print("\033[31m please enter a correct name \33[0m")
    return name

def intro():
    clear()
    drawing()
    name = chooseName()
    play(name, False)


def play(name,  word, score = 0, guess = [], times = 0):
    clear()
    y = 0
    answer = ''
    print(name + " Your score is " + str(score) + '\n')
    if not word:
         word = chooseWord()
    for k in word:
        y = y + 1
        if(y == 1 or check(k, guess)):
           print(k + ' '  , end = '')
        else:
            print("_ " , end = '')
    print("\n")
    drawingHangman(times)
    if(times == 12):
        print("You lose this round the word you were searching was " + word)
        return play(name , False , score - 1)
    print("\n\ncommand : ")
    print("/q : quit the game.")
    print("/l : Propose a letter.")
    print("/w : Propose a word.")
    while answer != '/q':
        answer = input('What are you doing ?')
        command = answer.split()
        if len(command) < 2:
            print("This command doesn't exist")
        else:
            if command[0] == '/q':
                print('Ty for playing !')
                return
            elif command[0] == '/l':
                if len(command) > 3:
                    print("plz enter a correct answer 'command + letter'")
                else: 
                    if check(command[1], word):
                        guess = is_in(guess, command[1])
                        play(name , word , score, guess, times)
                    else:
                        print("This letter is not in our word")
                        time.sleep(2)
                        play(name , word , score, guess, times + 1)
            elif command[0] == '/w':
                if len(command) > 3:
                    print("plz enter a correct answer 'command + word'")
                else:
                    if(word == command[1]):
                        print('Well played you discover the word !')
                        time.sleep(2)
                        play(name , False , score + 1)
                    else:
                        print('This is not the right word :c')
                        time.sleep(2)
                        play(name , word , score, guess, times + 1)

            else:
                print("This command doesn't exist")
    
    # Check if the letter exist in a list 
def check(letter , guess):
    for x in guess:
        if letter == x:
            return True
    return False

    # Push in the guess listif the letter isn't on it 
def is_in(guess, letter):
    for x in guess:
        if letter == x:
            print("You can't say 2 times the same letters :/") 
            time.sleep(2)
            return guess
    guess.append(letter)
    return guess

    # you can put all the words you want and the code will randomly chose one
def chooseWord(): 
    words = ["tracteur", "homme", "femme"]
    return random.choice(words)

# All the hangman position 
def drawingHangman(times = 0):
    tab = [[], ["---"], ['|',"---"], ['|','|', "---"], ['|','|','|', "---"], ['|','|','|','|', "---"],['|','|','|','|','|', "---"],['---','|','|','|','|','|', "---"],['---','|  |','|','|','|','|', "---"],['---','|  |','|  o','|','|','|', "---"],['---','|  |','|  o',"| /|\ " ,'|','|', "---"],['---','|  |','|  o', "| /|\ " , '|  |','|', "---"],['---','|  |','|  o','| /|\ ','|  |','| /-\ ', "---"]]
    for i in tab[times]:
        print(i)

intro()