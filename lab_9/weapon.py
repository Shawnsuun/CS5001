from random import *
from type_writter import *

'''
Weapon class. Provides an attack value, but decreases durablity each use
Attributes: name, strength, durability, critical
Methods: attack
''' 

class Weapon:
	def __init__(self, name = "generic dagger", strength = 1, durability = 2, critical = False):
		"""
		constructor of class Weapon
		"""
		self.name = name
		self.strength = strength
		self.durability = durability 
		self.critical = critical


	def attack(self):
		"""
		return the value of damage when the weapon is used to attack

		"""		
		if self.durability <= 0:
			print_pause(self.name + " has no durability!")
			return 0
		self.durability -= 8
		#calculate possible addtional critical attack value
		add_harm = 0
		if self.critical and randint(0,1) == 0:
			add_harm += randint(self.strength / 2, self.strength)
			print_pause(self.name + " caused " + str(add_harm) + " critical strike!!!")
		#damage include the basic damage of the weapon and possible critical attack value
		return randint(1, self.strength) + add_harm


	def __str__(self):
		"""
		return the the string info of the weapon

		"""		
		return self.name + " strength:" + str(self.strength) + " durability:" + str(self.durability)




