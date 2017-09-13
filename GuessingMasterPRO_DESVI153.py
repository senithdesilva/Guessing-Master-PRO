#Importing 2 files called random and sys for later use.
import random
import sys
tries = [] #This is a Array which stores value in a list.
           #This Array is used to store the number of attempts the user has taken

# Total I have created 8 Functions for this program.
# Function get_guess() and Function check_guess() are the main two functions of this program

#difficulty() Function check what level the user have selected.  
def difficulty(answer):
    while True:
        global ran_no
        if answer != 1 and answer != 2 and answer !=3:
            print('Invalid Input. Please Re-enter!')
            main_two()
        else:
            if answer == 1:
                max_number = 10
                level = answer
                ran_no = random.randint(0,max_number)
                get_guess(max_number, level)
                
            if answer == 2:
                max_number = 50
                level = answer
                ran_no = random.randint(0,max_number)
                get_guess(max_number, level)
                

            if answer == 3:
                max_number = 100
                level = answer
                ran_no = random.randint(0,max_number)
                get_guess(max_number, level)
                

    return ran_no

#mode() Function will output the level that the user has selected.  
def mode(level):
    if level == 1:
        print('Easy Mode 0 to 10')
    elif level == 2:
        print('Medium Mode 0 to 50')
    elif level == 3:
        print('Hard Mode 0 to 100')
    return level

#get_guess() Function is the first base function in this program.
#This will ask the users guess and if the guess is over the max number, it will re-prompt.
#Further it will validate by not allowing the user to enter a non-numeric value. 
def get_guess(max_number, level):
    mode(level)
    while True:
        try:
            guess = int(input('Guess? '))
            tries.append(guess) #Everytime the user enters a guess, it will be stored in the array tries.    
        except ValueError:
            print('Please enter a number')
        else:
            if guess > max_number:
                print('Guess? between 0 to', max_number)
            else:
                check_guess(guess)

#check_guess() Function is the second base function in this program.
#This function will check the users guess compared to the random number that is generated. 
def check_guess(guess): 
    turn = True
    while turn:
        if guess == ran_no:
           print('Correct\n')
           turn = False #If the guessed number and the random number is equal, this while loop will end.
           last_one()
           break
        elif guess < ran_no:
            print('Too Low')
            break
        elif guess > ran_no:
            print('Too High')
            break
        
#Due to couple of errors I had to separate the main Function into main_one(), main_two() and last_one()
def main_one():
        print('Welcome to Guess Master PRO 2016 ')
        print('Select Difficulty\n 1.Easy\n 2.Medium\n 3.Hard')
        
#I have used the TRY statement to further validate my WHILE loop.           
def main_two():
    while True:
        try:
            answer = int(input('Please choose a Level: \n'))
            difficulty(answer)
        except ValueError:
            #if the user enters a non-numeric value, the program will output this message.
            print('Please re-enter.\n    1 for Easy mode\n or 2 for Medium mode\n or 3 for Hard mode')
              
def last_one():
    print('You Took', len(tries) , 'Guesses') #len() function will give the no.of tries the user has taken.
    print('Your Guesses:', tries, '\n') #This will give the list of tries the user took.
    replay()
    
#The replay() function will ask the user if he/she wishes to play again.    
def replay():
    print('Do you wish to play again?')
    while True:
        play = input('If YES, press (y). If NO, press (n): \n')
        if play == 'y':
                   print('Lets Start Playing!\n')
                   del tries[:] #this will clear the array and start again
                   main_one() 
                   main_two()
        elif play == 'n':
                   print('Thank you for playing Guess Master PRO 2016')
                   print('See you soon')
                   sys.exit() #if the user doesn't want to play again, the program will stop. 
        else:
            print('Please Re-enter')

main_one() #This function will run first when the program starts.
main_two() #then this function will run second
        
