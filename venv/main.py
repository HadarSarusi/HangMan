""" co-programers : Evyatar Baruch , Hadar Sarusi """
import math # We are importing math for the exsept triger
import time # to stall the program
import pyautogui # the keybored conection to the program module
import Graphics  # We are importing the so called "Graphic"
import Dictionary # We are importing the list of words
import random # and at last the random lab for the randomness of the word selection
import pyfiglet # the graphics module

def concatenate(new_list):
    """
    this function print the list without the signs of a list.
    param: list of the correct guessed letters
    type: list
    return: the function doesn't return anything
    rtype: None
    """
    concatenated = ""
    for letter in new_list: # concatenating all the letters in the list into a string
        concatenated += letter
    print(concatenated) # the value of the list is printed without all the apostrophes

def valid(temp,word):
    """
    this function return a boolean value according to the letter legality and its existing in the word
    param: the guessed letter and the original word
    type: string,string1

    return: the function return a boolean value and a str in a tuple
    rtype: tuple(bool,str)
    """
    try: # when the letter contained in 'temp' is not follwing our legality the function will pass to the unique except and let the user know he entered unacceptable charecter two exceptional cases are the check for spaces and a clue request
        if(temp=="clue"): # when the user is requesting for a clue the function will return an indicator for the program that the user want to get a clue
            return True, "clue"
        if(temp==" "): # the first thing the program do is to chack if there is any spaces in the word so in case there are spaces the function will consider it as a valid guess
            return True, "print"
        if(not(temp.isalpha())): # if the guess is a digit,the program will print an error messege by exsepting as value error and if the user entered a mixed string by excepting as type error
            print(int(temp) + " ") # value error / type error
        elif(len(temp) > 1): # if the user enter more then one charcter print an error messege by excepting as over flow error
            temp = math.exp(1000) # overflow error
        else: # the letter is legal
            try: # when the guessed letter isn't in the original word the programp will pass to the ecxcept as a value error
                if (word.index(temp) != None):  # if the letter is in the word the index function will return the location of the letter otherwise the index function return "None" and pass to the right except
                    print(temp) # a validation for the user that the letter wasn't an exception
                    return True, "print" #  a validation for the program that the letter wasn't an exception by retunning 'print'
            except ValueError: # when the guessed letter isn't in the original word the function will print a message for the user ang return 'False' as an indicator it's not a currect guess
                print("boohoo,you suck at this game\nyou should consider quit the game")
                return False, "print"
    except OverflowError as err: # when there is exception of a Overflow Error the function will let the user know
        print(err)
    except TypeError as err:  # when there is exception of a Type Error the function will let the user know
        print(err, temp)
    except ValueError as err: # when there is exception of a Value Error the function will let the user know
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
    final = 0 # final grade
    garde_sheet = [] # list of the user grades
    print("wellcome to the game")
    print(pyfiglet.figlet_format(" Hang - man", font="doh", width=200), end="")
    user_name= input("Enter user name: ")
    x,y = pyautogui.position() # the coordination of the game in this particular moment
    pyautogui.click(x,y)  # a click in this particular place for the 'hotkey' function
    pyautogui.hotkey('alt', 'd') # deleting all the output
    game = "y" # a variable for checking if the user would like to play again
    while (game == "y"):  # while the user want to keep going eith the play
        right_guess = 0
        actual_cycle = 0# the actual number of guesses (necessary because of double lettrs)
        temp=" " # a variable for check in the first iteration if there any spaces in the word also in the rest of them the variabla contain the geussed letter
        valid_input = False # a variable that used to check if the user entered a valid input
        while(not(valid_input)): # while the user entered the wrong input, the loop ask him to put another one input and let him know
            level = input("Select your level: \n1 - easy\n2 - medium\n3 - hard\n4 - chinese\n")
            if(level > "0" and level < "5" and len(level) == 1): # if the input is correct the variable "valid_input" will flip
                valid_input = True
                level = int(level) # convert the variable from 'str' to 'int' in order to calculate the num of clues
            else:
                print("TypeError ,please enter a number from the appropriate range") # while the input's user does't correct the program let him know
        frequency = [ 3, 6, 9, 3000] # the list of denominators for the frequency of clues by the level
        while(valid_input): # while the user entered the wrong input, the loop ask him to put another one input and let him know
            gender = input("would you like to wear pents or skirt?: ")
            if(gender.lower() == "skirt" or gender.lower() == "pents"):# if the input is correct the variable "valid_input" will flip
                valid_input = False
            else:
                print("TypeError ,please enter 'skirt' or 'pents'")
        while (not (valid_input)): # while the user entered the wrong input, the loop ask him to put another one input and let him know
            selection = (input("select your preference: \n1 - names\n2 - countries\n3 - animals\n4 - plants\n5 - phrases\n"))
            if (selection > "0" and selection < "6" and len(selection) == 1): # if the input is correct the variable "valid_input" will flip
                valid_input = True
                selection = int(selection)# convert the variable from 'str' to 'int' in order to specified the user's selection subject
            else:
                print("TypeError ,please enter a number from the appropriate range")
        selection -= 1 # match the user's selection to the indexes
        choices = [Dictionary.names, Dictionary.countries, Dictionary.animals, Dictionary.plants, Dictionary.phrase] # a list of themes that imported from "Dictionary"
        choices_names = ["names", "countries", "animals", "plants", "phrases"] # to print the specific theme that have been choosen by the user
        words = choices[selection] # a pointer to the specific dictionary theme
        counter_of_successe = 0 # a counter used to count every currect guess
        word = words[random.randint(0,len(words)-1)] # a random ward from the specific dictionary theme
        word = word.lower() # make sure the ward is lower case
        copy_word = word # a copy of the random word (one will be alter and one won't)
        clue_counter = int(len(word)/(frequency[level-1])) # define the number of available clues
        initial_clue = int(len(word)/(frequency[level-1]))
        number = 7 # the maximum number of guesses
        new_list = list("_"*len(word)) # a list of '_' in the length of the word
        guessed_letters = "" # a string of the guessed letters
        counter = 0 #the counter of incorrect geusses
        cycle_counter=0 # a counter which counts every iteration (WARNING!: not accurate)
        #try: #
        while (counter < number): # while the incorrect geusses smaller than the attempts
            if(cycle_counter==1): # in the first geuss
                for i in range(3): # for 3 times, print three dots
                    print(".", end = " ")
                    time.sleep(1 / 2) # stalling half a second between each dot
                pyautogui.hotkey('alt', 'd') # deleting all the output

                print("* in each attempt type a single letter\n* for a clue type \"clue\" \n\nyou may have 7 attempts about " + choices_names[selection]+ " and ",clue_counter, "clues\npress Enter to continue")
                input()
                pyautogui.hotkey('alt', 'd') # deleting all the output
                concatenate(new_list)
                temp = input("have a guess: ")
            new_word = "" # concatenate the wrong geusses
            start_range = 0 # the range's start of the indexes in which the program is going to look for the letter
            temp = temp.lower() # all the uppercase letters becomes to lowercase letters
            try: # if we get from the second 'if' None there will be value error
                if(len(temp) == 1): # in order to prevent overflow mistakes to be inserted into 'geussed_letters'
                    if(guessed_letters.index(temp) != None and cycle_counter!=0 ): # if the letter is existing letter
                        temp = input("you guessed this letter already\nguess a diffrent letter: ")
                int(" ") # in order to continue into the except explicitly
            except ValueError:
                if(len(temp) == 1): # only when the temp is one character I'll concatenate it to 'guessed_letters'
                #if(len(temp) != 1):
                   # pass
               # else:
                    guessed_letters += temp
                result , printable = valid(temp,copy_word) # get two values from the valid function ensure validation
                if (not(result)): # if the resule (boolean value) is False - meaning there was an exception
                    counter+=1
                else:
                    if(printable == "clue" and clue_counter > 0): # if printable (string) is eqeul to "clue" and "clue_counter" is bigger then 0
                        clue_counter-=1
                        temp = copy_word[random.randint(0,len(copy_word)-1)] # a random word from the chosen dict
                        guessed_letters += temp
                    elif(printable == "clue" and clue_counter == 0): # in case the user used all his clue
                        print("it's an intervention, you have a clues addiction and from now on you are on rehab")
                    for letter in copy_word:#A. check if the geussed letter is in the origion word, B. update the founded letters and delete those letters from the copy origion word.
                        if(letter==temp):
                            counter_of_successe +=1
                            new_list[word.index(temp,start_range)]=temp
                            start_range = word.index(temp, start_range)+1
                        else:
                            new_word+=letter
                    copy_word=new_word
                if(counter_of_successe == len(word)):
                    actual_cycle += 1
                    right_guess += 1
                    pyautogui.hotkey('alt', 'd')
                    for num in range(4):
                        time.sleep(0.5)
                        pyautogui.hotkey('alt', 'd')
                        print(pyfiglet.figlet_format("CONGRATULATION!", font="banner3-D", width=200), end="")
                    print("you got it\nthe word is:\""+word+"\"\nyou saved this ugly humen")
                    if (gender.lower() == "pents"):
                        print(Graphics.hang_human_pents[counter])
                    else:
                        print(Graphics.hang_human_skirt[counter])
                    game = input("would you be palying again?\nEnter \"y\" or \"n\"\n\"y\" - yes \"n\" - no\n")
                    break
                elif(cycle_counter != 0 and result == True and printable != "clue" and printable != "exception"):
                    print("well done ,good geuss ")
                    right_guess += 1
                if(cycle_counter>0):
                    concatenate(new_list)
                if(cycle_counter != 0 and printable == "print"):
                    actual_cycle +=1
                    if(gender.lower() == "pents" ):
                        print(Graphics.hang_human_pents[counter])
                    else:
                        print(Graphics.hang_human_skirt[counter])

                if(counter < number and cycle_counter > 0):
                    for i in range(3):
                        print(".", end=" ")
                        time.sleep(1)
                    pyautogui.hotkey('alt', 'd')
                    if (cycle_counter > 0):
                        concatenate(new_list)
                    print("you have ",number-counter," attempts left and ",clue_counter ," clues")
                    print("letters you have guesed already:",end = " ")
                    for been_there_dune_that in guessed_letters:
                        if (been_there_dune_that != " "):
                            print(been_there_dune_that, end=" ")
                    print(" ")
                    temp = input("have another guess: ")
            cycle_counter+=1
        if(counter>=7):
            pyautogui.hotkey('alt', 'd')
            for num in range(4):
                time.sleep(0.5)
                pyautogui.hotkey('alt', 'd')
                print(pyfiglet.figlet_format("LOSER!", font="banner3-D", width=200), end="")
            print("the word was \""+word+"\" \nnext time try something you actually good at like mikado or bingo")
            if (gender.lower() == "pents"):
                print(Graphics.hang_human_pents[counter])
            else:
                print(Graphics.hang_human_skirt[counter])
            while ((valid_input)):  # while the user entered the wrong input, the loop ask him to put another one input and let him know
                game = input("if you insist to continue enter \"y\" else \"n\"\n\"y\" - yes \"n\" - no\n")
                game = game.lower()
                if (game == "y" or game == "n"):
                     valid_input = False
                else:
                    print("TypeError ,please enter 'y' or 'n'")
        #except ValueError as err: #catch(string err)
           # print(err)
        pyautogui.hotkey('alt', 'd')
        try: # if the initial_clue==0
            #actual_cycle = number - (number-counter) + counter_of_successe # the num of cycle include rhe double letters
            match level: # match by the variable 'level'
                case 1:
                    grade = (right_guess/actual_cycle) * 90 + (clue_counter / initial_clue) * 10
                case 2:
                    grade = (right_guess/actual_cycle) * 82 + (clue_counter / initial_clue) * 18
                case 3:
                    grade = (right_guess/actual_cycle) * 75 + (clue_counter / initial_clue) * 25
                case 4:
                    grade = (right_guess/actual_cycle) * 95 + 5
        except ZeroDivisionError: # if the dinumerator == 0
            match level:
                case 1:
                    grade = (right_guess/actual_cycle) * 90 + 10
                case 2:
                    grade = (right_guess/actual_cycle) * 82 + 18
                case 3:
                    grade = (right_guess/actual_cycle) * 75 + 25
        garde_sheet.append(grade) # append to the list the grade
    for total in garde_sheet:
        final += total # sum the elements of grades
    final = final/len(garde_sheet) # do the avarege grades
    score_file = open(r"score", "r") #open file for read
    for n in range(10): # cutting off the insignificin parts of every line
        red = score_file.readline() # first read
        red = red[:len(red) - 1] # cutting off the last character
        details.append(red.split(":")) # append and split the line into two parts using ':' as the pivet value
    for n in details: # go throuh every element in the list
        details_the_sec.append({"name": n[0], "score": float(n[1])}) # converting from [[],[],...] to [{},{},{},...]
    details_the_sec.append({"name": user_name, "score": float(final)}) # inserting the current user details
    details_the_sec.sort(key=lambda indicator: indicator["score"], reverse=True) # sorting according to the score value
    score_file.close() # closing the file
    score_file = open(r"score", "w") #open file for write
    for n in range(10): # go throuh the first 10 indexes and writing them into the file
        temper = details_the_sec[n] # a temporary variable for each dictionary
        score_file.write(str(temper["name"]) + ":" + str(temper["score"]) + "\n") # writing the relevant iformation in the currect format
    score_file.close() # closing the file
    score_file = open(r"score", "r") #open file for read
    print(pyfiglet.figlet_format("10 top players:",font = "roman",width = 200)) # printing the list of the ten top player
    print(score_file.read())

if __name__ == "__main__":
    main()