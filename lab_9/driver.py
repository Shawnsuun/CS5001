from random import *
from type_writter import *

from character import Character
from weapon import Weapon

def game():
    '''
    The driver of the game
    Initialize weapons and characters
    Let user select 2 characters and set weapons for them
    The characters will fight until one of them is dead
    '''    

    #initialize all weapons
    long_claw = Weapon("Long Claw", 70, 40)
    elven_dagger = Weapon("Elven Dagger", 80, 26)
    war_hammer = Weapon("War Hammer", 60, 70)
    knight_sword = Weapon("Knight Sword", 50, 50)

    elven_dagger.critical = True

    #put all weapons in a list
    weapons = [long_claw, elven_dagger, war_hammer, knight_sword]

    #initialize all characters
    knight = Character("Light Knight", 500, 80)
    assassin = Character("Assassin", 350, 150)
    orc = Character("Orc", 600, 50)
    elven = Character("Elven", 425, 85)

    elven.magic = True
    knight.healing = True

    #put all characters in a list
    characters = [knight, assassin, orc, elven]


    #choose your character
    valid_selections = ["1", "2", "3", "4"]
    print_pause("\nPlease select your character:")
    for character in characters:
        print_pause(str(characters.index(character) + 1) + " " + str(character)) 
    #parse user input and handle error
    while True:
        selection = input("Please enter a number to select\n")
        try:
            if (selection not in valid_selections):
                raise ValueError("Please input number in 1 ~ 4")
            character1 = characters[int(selection) - 1]
            characters.pop(int(selection) - 1)
            break
        except ValueError as ex:
            print(ex)

    #select weapon for your character
    print_pause("\nPlease select the weapon for your character:")
    for weapon in weapons:
        print_pause(str(weapons.index(weapon) + 1) + " " + str(weapon))
    #parse user input and handle error
    while True:
        selection = input("Please enter a number to select\n")
        try:
            if (selection not in valid_selections):
                raise ValueError("Please input number in 1 ~ 4")
            weapon1 = weapons[int(selection) - 1]
            character1.giveWeapon(weapon1)
            weapons.pop(int(selection) - 1)
            break
        except ValueError as ex:
            print(ex)

    #choose the opponent
    valid_selections = ["1", "2", "3"]
    print_pause("\nPlease select the opponent:")
    for character in characters:
        print_pause(str(characters.index(character) + 1) + " " + str(character))
    #parse user input and handle error
    while True:
        selection = input("Please enter a number to select\n")
        try:
            if (selection not in valid_selections):
                raise ValueError("Please input number in 1 ~ 3")            
            character2 = characters[int(selection) - 1]
            break
        except ValueError as ex:
            print(ex)


    #select weapon for the opponent
    print_pause("\nPlease select the weapon for the opponent:")
    for weapon in weapons:
        print_pause(str(weapons.index(weapon) + 1) + " " + str(weapon))
    #parse user input and handle error
    while True:
        selection = input("Please enter a number to select\n")
        try:
            if (selection not in valid_selections):
                raise ValueError("Please input number in 1 ~ 3") 
            weapon2 = weapons[int(selection) - 1]
            character2.giveWeapon(weapon2)
            break
        except ValueError as ex:
            print(ex)
    #let two characters fight
    character1.fight(character2)


def main ():
    '''
    The main function of the game
    '''        
    game()
    

#call main funtion
main()