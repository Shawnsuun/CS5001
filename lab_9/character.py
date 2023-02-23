from random import *
from type_writter import *

'''
This is a character class for a simple battle game
Attributes: name, hitPoints, strength, alive, weapon, magic, healing
Methods: fight, take_damage, magic_attack, heal, fight
''' 

class Character:
    def __init__(self, name = "Ward", hitPoints = 5, strength = 5, alive = True, weapon = None, magic = False, healing = False):
        """
        constructor of class Character
        """        
        self.name = name
        self.hitPoints = hitPoints
        self.strength = strength
        self.alive = alive
        self.weapon = weapon
        self.magic = magic
        self.healing = healing


    def __str__(self):
        """
        return the the string info of the character
        """         
        return self.name + " HP:" + str(self.hitPoints) + " ATK:" + str(self.strength)


    def giveWeapon(self, weapon):
        """
        set a weapon for a character
        """            
        if self.weapon == None:
            print_pause(self.name + " has equiped " + weapon.name)
        else:
            print_pause(self.name + " has switched weapon " + self.weapon.name + " into " + weapon.name)
        self.weapon = weapon

        
    def take_damage(self, damage):
        """
        let a character take damage
        """             
        self.hitPoints -= damage
        if self.hitPoints <= 0:
            self.hitPoints = 0
            self.alive = False


    def magic_attack(self, opt):
        """
        let a character use magic attack to opponent for 50% chance during attack
        """          
        if (self.magic and randint(0, 1) == 1 and opt.alive):
            magic_damage = randint(0,50)
            print_pause(self.name + " used fire magic!!")
            print_pause(str(opt) + " took " + str(magic_damage) + " magic damage")
            opt.take_damage(magic_damage)
            

    def heal(self):
        """
        let a character heal instead of attack when hitPoints is lower than 40 during attack
        """           
        if (self.healing and self.hitPoints < 40 and self.alive):
            heal_val = randint(0,50)
            print_pause(self.name + "healed " + str(heal_val) + " hit points!!")
            self.hitPoints += heal_val
            return True
        return False


    def fight(self, opt):
        """
        let two character fight until one of them is not alive, print the process and the winner
        """          
        while (self.alive and opt.alive):
            healed = self.heal()
            if not healed:
                print_pause(str(self) + " attacked " + str(opt))
                opt_damage = randint(0, self.strength) + self.weapon.attack()
                print_pause(opt.name + " took " + str(opt_damage) + " damage")
                opt.take_damage(opt_damage)
                self.magic_attack(opt)

            if opt.alive:
                healed = opt.heal()
                if not healed:
                    char_damage = randint(0, opt.strength) + opt.weapon.attack();
                    print_pause(str(opt) + " attacked " + str(self))
                    print_pause(self.name + " took " + str(char_damage) + " damage")
                    self.take_damage(char_damage)
                    opt.magic_attack(self)
            else:
                break

        print_pause("The winner is:")
        if self.alive: 
            print_pause(str(self))
        else:
            print_pause(str(opt))


