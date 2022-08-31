""" co-programers : Evyatar Baruch , Hadar Sarusi """
import math # We are importing math for the exsept triger
import time # to stall the program
import pyautogui # the keybored conection to the program module
import Graphics # We are importing the so called "Graphic"
import Dictionary # We are importing the list of words
import random # and at last the random lab for the randomness of the word selection
import pyfiglet # the graphics module
#import os # in order to clean the screen

def concatenate(new_list):
    """
    this function print the list without the apostrophes of a list.
    param: list of the correct guessed letters
    type: list
    return: the function doesn't return anything
    rtype: None
    """
    concatenated = ""
    for letter in new_list:
        concatenated += letter
    print(concatenated)

def valid(temp,word):
    """
    this function return a tuple of a boolean and a string according to the letter legality and its existing in the wordin case 'temp' is not follwing our legality the function will pass to the unique except and let the user know he entered unacceptable charecter, two exceptional cases are the check for spaces and clues request
    param: the guessed letter and the original word
    type: string,string
    return: the function return a boolean value and a str in a tuple
    rtype: tuple(bool,str)
    """
    try:
        if(temp=="clue"):
            return True, "clue"
        if(temp==" "): # the first thing the program do is to chack if there is any spaces in the word so in case there are spaces the function will consider it as a valid guess
            return True, "print"
        if(not(temp.isalpha())):
            print(int(temp) + " ") # value error / type error
        elif(len(temp) > 1):
            temp = math.exp(1000) # overflow error
        else: # the letter is legal
            try: # when the guessed letter isn't in the original word the programp will pass to the ecxcept as a value error
                if (word.index(temp) != None):  # if the letter is in the word the index function will return the location of the letter otherwise the index function return "None" and pass to the right except
                    print(temp)
                    return True, "print" #  a validation for the program that the letter wasn't an exception by retunning 'print'
            except ValueError:
                print("boohoo,you suck at this game\nyou should consider quit the game")
                return False, "print"
    except OverflowError as err:
        print(err)
    except TypeError as err:
        print(err, temp)
    except ValueError as err:
        print(err)
    return True ,"exception" # if the function reached this point it's an indicator there was an exception and in order to indicate it the function will return 'exception'

def main():
    """
    this program is a game of 'hangman' for one user ,the game work in simple way - the user is asked to insert the clothing preferaion ,the level of the game and the theme he would like the word to be choosen randomly from
    the user get 7 incurrect guesses in order to guess the word and a few clues depend on the level he choose and the game is officially started
    """
    user_name = ""
    details =[] # the raw details of the 10 top list
    details_the_sec = [] # the second stage of the details ,necessary for sorting and locaiting the new user
    final = 0
    garde_sheet = []
    print("wellcome to the game")
    print(pyfiglet.figlet_format(" Hang - man", font="doh", width=200), end="")
    user_name= input("Enter user name: ")
    # os.system('cls') [windows] / os.system('clear')
    pyautogui.hotkey('alt', 'd')
    game = "y" # a variable for checking if the user would like to play again
    while (game == "y"):
        right_guess = 0
        actual_cycle = 0 #(necessary because of double lettrs)
        temp=" " # a variable used to check in the first iteration if there any spaces in the word and also in the rest of the iterations the variabla contain the geussed letter
        valid_input = False
        while(not(valid_input)): # while the user entered the wrong input, the loop ask him to put another one input and let him know
            level = input("Select your level: \n1 - easy\n2 - medium\n3 - hard\n4 - chinese\n")
            if(level > "0" and level < "5" and len(level) == 1):
                valid_input = True
                level = int(level)
            else:
                print("TypeError ,please enter a number from the appropriate range")
        frequency = [ 3, 6, 9, 3000] # the list of denominators for the frequency of clues by the level
        while(valid_input): # while the user entered the wrong input, the loop ask him to put another one input and let him know
            gender = input("would you like to wear pants or skirt?: ")
            if(gender.lower() == "skirt" or gender.lower() == "pants"):
                valid_input = False
            else:
                print("TypeError ,please enter 'skirt' or 'pants'")
        while (not (valid_input)): # while the user entered the wrong input, the loop ask him to put another one input and let him know
            selection = (input("select your preference: \n1 - names\n2 - countries\n3 - animals\n4 - plants\n5 - phrases\n"))
            if (selection > "0" and selection < "6" and len(selection) == 1):
                valid_input = True
                selection = int(selection)
            else:
                print("TypeError ,please enter a number from the appropriate range")
        selection -= 1
        choices = [Dictionary.names, Dictionary.countries, Dictionary.animals, Dictionary.plants, Dictionary.phrase]
        choices_names = ["names", "countries", "animals", "plants", "phrases"] # to print the specific theme that have been choosen by the user
        words = choices[selection]
        counter_of_successe = 0
        word = words[random.randint(0,len(words)-1)]
        word = word.lower()
        copy_word = word
        available_clues = int(len(word)/(frequency[level-1]))
        initial_clue = int(len(word)/(frequency[level-1]))
        max_guesses = 7
        successfully_guessed = list("_"*len(word))
        guessed_letters = ""
        wrong_guesses = 0
        cycle_counter=0
        while (wrong_guesses < max_guesses):
            if(cycle_counter==1):
                for i in range(3):
                    print(".", end = " ")
                    time.sleep(1 / 2)
                # os.system('cls') [windows] / os.system('clear')
                pyautogui.hotkey('alt', 'd')
                print("* in each attempt type a single letter\n* for a clue type \"clue\" \n\nyou may have 7 attempts about " + choices_names[selection]+ " and ",available_clues, "clues\npress Enter to continue")
                input()
                #os.system('cls') [windows] / os.system('clear')
                pyautogui.hotkey('alt', 'd')
                concatenate(successfully_guessed)
                temp = input("have a guess: ")
            unguessed_letters = "" 
            start_range = 0 
            temp = temp.lower() 
            try: # if we get from the second 'if' None there will be value error
                if(len(temp) == 1): # in order to prevent overflow mistakes to be inserted into 'geussed_letters'
                    if(guessed_letters.index(temp) != None and cycle_counter!=0 ): 
                        temp = input("you guessed this letter already\nguess a diffrent letter: ")
                int(" ") # in order to continue into the except explicitly
            except ValueError:
                if(len(temp) == 1):
                    guessed_letters += temp
                result , printable = valid(temp,copy_word) 
                if (not(result)): # if the resule (a boolean value) is False - meaning there was an exception
                    wrong_guesses+=1
                else: 
                    if(printable == "clue" and available_clues > 0):
                        available_clues-=1
                        temp = copy_word[random.randint(0,len(copy_word)-1)] 
                        guessed_letters += temp
                    elif(printable == "clue" and available_clues == 0):
                        print("it's an intervention, you have a clues addiction and from now on you are on rehab")
                    for letter in copy_word:#A. check if the geussed letter is in the origion word, B. update the founded letters and delete those letters from the copy origion word.
                        if(letter == temp):
                            counter_of_successe +=1
                            successfully_guessed[word.index(temp,start_range)]=temp
                            start_range = word.index(temp, start_range)+1
                        else:
                            unguessed_letters+=letter
                    copy_word= unguessed_letters
                if(counter_of_successe == len(word)):
                    actual_cycle += 1
                    right_guess += 1
                    pyautogui.hotkey('alt', 'd')
                    for num in range(4):
                        time.sleep(0.5)
                        pyautogui.hotkey('alt', 'd')
                        print(pyfiglet.figlet_format("CONGRATULATION!", font="banner3-D", width=200), end="")
                    print("you got it\nthe word is:\""+word+"\"\nyou saved this ugly humen")
                    if (gender.lower() == "pants"):
                        print(Graphics.hang_human_pents[wrong_guesses])
                    else:
                        print(Graphics.hang_human_skirt[wrong_guesses])
                    game = input("would you be palying again?\nEnter \"y\" or \"n\"\n\"y\" - yes \"n\" - no\n")
                    break
                elif(cycle_counter != 0 and result == True and printable != "clue" and printable != "exception"):
                    print("well done ,good geuss ")
                    right_guess += 1
                if(cycle_counter>0):
                    concatenate(successfully_guessed)
                if(cycle_counter != 0 and printable == "print"):
                    actual_cycle +=1
                    if(gender.lower() == "pants" ):
                        print(Graphics.hang_human_pents[wrong_guesses])
                    else:
                        print(Graphics.hang_human_skirt[wrong_guesses])
                if(wrong_guesses < max_guesses and cycle_counter > 0):
                    for i in range(3):
                        print(".", end=" ")
                        time.sleep(1)
                    pyautogui.hotkey('alt', 'd')
                    if (cycle_counter > 0):
                        concatenate(successfully_guessed)
                    print("you have ",max_guesses-wrong_guesses," attempts left and ",available_clues ," clues")
                    print("letters you have guesed already:",end = " ")
                    for been_there_dune_that in guessed_letters:
                        if (been_there_dune_that != " "):
                            print(been_there_dune_that, end=" ")
                    print(" ")
                    temp = input("have another guess: ")
            cycle_counter+=1
        if(wrong_guesses>=7):
            pyautogui.hotkey('alt', 'd')
            for num in range(4):
                time.sleep(0.5)
                pyautogui.hotkey('alt', 'd')
                print(pyfiglet.figlet_format("LOSER!", font="banner3-D", width=200), end="")
            print("the word was \""+word+"\" \nnext time try something you actually good at like mikado or bingo")
            if (gender.lower() == "pants"):
                print(Graphics.hang_human_pents[wrong_guesses])
            else:
                print(Graphics.hang_human_skirt[wrong_guesses])
            while ((valid_input)):  # while the user entered the wrong input, the loop ask him to put another one input and let him know
                game = input("if you insist to continue enter \"y\" else \"n\"\n\"y\" - yes \"n\" - no\n")
                game = game.lower()
                if (game == "y" or game == "n"):
                     valid_input = False
                else:
                    print("TypeError ,please enter 'y' or 'n'")
        pyautogui.hotkey('alt', 'd')
        try: # if the initial_clue==0
            match level: 
                case 1:
                    grade = (right_guess/actual_cycle) * 90 + (available_clues / initial_clue) * 10
                case 2:
                    grade = (right_guess/actual_cycle) * 82 + (available_clues / initial_clue) * 18
                case 3:
                    grade = (right_guess/actual_cycle) * 75 + (available_clues / initial_clue) * 25
                case 4:
                    grade = (right_guess/actual_cycle) * 95 + 5
        except ZeroDivisionError: 
            match level:
                case 1:
                    grade = (right_guess/actual_cycle) * 90 + 10
                case 2:
                    grade = (right_guess/actual_cycle) * 82 + 18
                case 3:
                    grade = (right_guess/actual_cycle) * 75 + 25
        garde_sheet.append(grade) 
    for total in garde_sheet:
        final += total # sum the elements of grades
    final = final/len(garde_sheet) 
    score_file = open(r"score", "r") 
    for n in range(10): # cutting off the insignificin parts of every line
        red = score_file.readline() 
        red = red[:len(red) - 1] # cutting off the last character
        details.append(red.split(":")) 
    for n in details: # go throuh every element in the list
        details_the_sec.append({"name": n[0], "score": float(n[1])}) # converting from [[],[],...] to [{},{},{},...]
    details_the_sec.append({"name": user_name, "score": float(final)}) # inserting the current user details
    details_the_sec.sort(key=lambda indicator: indicator["score"], reverse=True) # sorting according to the score value
    score_file.close() # closing the file
    score_file = open(r"score", "w") 
    for n in range(10): # go throuh the first 10 indexes and writing them into the file
        temper = details_the_sec[n]
        score_file.write(str(temper["name"]) + ":" + str(temper["score"]) + "\n") # writing the relevant iformation in the currect format
    score_file.close() # closing the file
    score_file = open(r"score", "r")
    print(pyfiglet.figlet_format("10 top players:",font = "roman",width = 200)) 
    print(score_file.read())

if __name__ == "__main__":
    main()