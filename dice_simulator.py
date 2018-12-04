# Ellis Nielsen         12-3-18
# this is a dice simulator for anything it does not display a dice on the screen, but man does it work
import random
import sys
import time


# get how many rolls that the users want to roll
def start():
    dice_num = float(input('How many dice do you want to roll? 1,2,3,4?: '))
    if dice_num == 1:
        dice_1()
    elif dice_num == 2:
        dice_2()
    elif dice_num == 3:
        dice_3()
    elif dice_num == 4:
        dice_4()
    else:
        error_end()


# this is the list of rolls and the function that picks the roll
def dice():
    dice_list_1 = ['1', '2', '3', '4', '5', '6']
    return random.choice(dice_list_1)


# this is for one dice roll
def dice_1():
    dice_1_roll_1 = int(dice())
    time.sleep(.5)
    print(f'The first roll is: {dice_1_roll_1}')
    time.sleep(.5)
    print(f'The total is: {dice_1_roll_1}')


# this is for two dice rolls
def dice_2():
    dice_2_roll_1 = int(dice())
    dice_2_roll_2 = int(dice())
    time.sleep(.5)
    print(f'The First roll is {dice_2_roll_1}')
    time.sleep(.5)
    print(f'The Second roll is {dice_2_roll_2}')
    time.sleep(.5)
    print(f'The total is: {dice_2_roll_1+dice_2_roll_2}')


# this is for three dice rolls
def dice_3():
    dice_3_roll_1 = int(dice())
    dice_3_roll_2 = int(dice())
    dice_3_roll_3 = int(dice())
    time.sleep(.5)
    print(f'The First roll is {dice_3_roll_1}')
    time.sleep(.5)
    print(f'The Second roll is {dice_3_roll_2}')
    time.sleep(.5)
    print(f'The Third roll is {dice_3_roll_3}')
    time.sleep(.5)
    print(f'The total is: {dice_3_roll_1+dice_3_roll_2+dice_3_roll_3}')


# this is for four dice rolls
def dice_4():
    dice_4_roll_1 = int(dice())
    dice_4_roll_2 = int(dice())
    dice_4_roll_3 = int(dice())
    dice_4_roll_4 = int(dice())
    time.sleep(.5)
    print(f'The First roll is {dice_4_roll_1}')
    time.sleep(.5)
    print(f'The Second roll is {dice_4_roll_2}')
    time.sleep(.5)
    print(f'The Third roll is {dice_4_roll_3}')
    time.sleep(.5)
    print(f'The fourth roll is {dice_4_roll_4}')
    time.sleep(.5)
    print(f'The total is: {dice_4_roll_1+dice_4_roll_2+dice_4_roll_3+dice_4_roll_4}')


# displays a message if the user inputs an issue whit the rolls
def error_end():
    print("I don't know what you mean")
    start_over = input("Do you want to start over? Yes or No: ")
    if start_over in ('yes', 'Yes', 'y'):
        final_start()
    else:
        sys.exit(0)


# starts the whole program
def final_start():
    start()
    again = input("do you want to roll again? Yes or no: ")
    if again in ('Yes', 'yes', 'y'):
        final_start()
    else:
        sys.exit(0)


final_start()
