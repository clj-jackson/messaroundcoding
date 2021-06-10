import click
import _pickle as pickle
import os
import time
import json
import math
import sys
from random import randint

def print_delay(string, delay):
  for character in string:
    print(character, end="", flush=True)
    time.sleep(delay) 

def loading_bar():
	toolbar_width = 40

	sys.stdout.write("[%s]" % (" " * toolbar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (toolbar_width+1))

	for i in range(toolbar_width):
		time.sleep(0.1)
		sys.stdout.write("■")
		sys.stdout.flush()

	sys.stdout.write("]\n")

def main_menu():
	while True:
		try:
			click.clear()
			x = int(input("Super Hero Simulator!\n\nMain Menu:\n\n1)Create Account\n2)Load Account\n3)Exit\n\nInput:\t"))
			time.sleep(0.5)
			click.clear()
			break
		except ValueError:
			click.clear()
			print("\nIncorrect input.\n")
			time.sleep(0.5)
	return x

def exit_game():
	sys.exit("Thank you for playing!\n\n")

class opening_sequence:
	
	def __init__(self, name, age, supertype, filename):
		self.name = name
		self.age = age
		self.supertype = supertype
		self.filename = filename
		self.data = {"Name": 0, "Age": 0, "Supertype": 0, "Filename": 0}

	def introduction(self):

		print_delay("Welcome, have you ever wanted to be a super hero?\n\nWho are we kidding? Of course you have! Everyone has, and in this game you can. You will create a superhero and fight the evil in this world. \n\nAs you progress through the game your superhero will become stronger and fight stronger foes, but first lets create your hero. We hope you enjoy!\n", 0.05)

		input("\n\nPress the 'enter' key to continue...")

		click.clear()

		print_delay("Hello, welcome to the super hero creation lab. I am your personal helper, 'Jade' and I will help you become the greatest superhero the world has ever known.\n\n", 0.05)

		while True:
			print_delay("Firstly, let me teach you how to respond, move around the world and use your powers (once they have been given to you), all you need to do is type the number corresponding to what you would like to choose/do. Here is an example:\n\n", 0.05)

			x = input("Do you understand what I have told you?\n\n1)Yes\n2)No\n\nInput:\t")

			if x == "1":
				print("\n\nSee it's that easy!")
				break
			elif x == "2":
				print("\n\nMy apologies, let me try to explain it to you again.")
				time.sleep(2)
				click.clear()
			elif x != "1" and x != "2": 
				print("\n\nThat was an incorrect input, I will try to explain this to you again")
				time.sleep(2)
				click.clear()

	def super_creation(self):
		click.clear()
		print_delay("Now it is time to make you the superhero you've always wanted to be.\n\nHere you will complete a form which will allow us to have some important data from you before we give you your powers.\n\n", 0.05)

		time.sleep(2)


		while True:
			try:
				click.clear()
				self.name = input("Question 1: What is your name?\n\nInput:\t")
				self.data["Name"] = self.name
				self.age = int(input("\n\nQuestion 2: What is your age?\n\nInput:\t"))
				self.data["Age"] = self.age
				self.supertype = int(input("\n\nQuestion 3: From the options below, which power would you rather begin with? (Note: This cannot be changed at a later time)\n\n1)Super speed\n2)Super strength\n3)Invisibility\n4)Levitation/flight\n5)Impenetrability\n\nInput:\t"))
				if self.supertype > 6 or self.supertype < 1:
					raise SyntaxError
				self.data["Supertype"] = self.supertype
				self.filename = input("\nQuestion 4: What would you like to name your save file, so that we can load your data in the future.\n\nInput:\t")
				self.data["Filename"] = self.filename

				click.clear()
				break

			except SyntaxError:
				print("Incorrect input.")
				time.sleep(2)
			except:
				print("Incorrect input.")
				time.sleep(2)

		print("Processing data...")

		loading_bar()

		time.sleep(2)

		click.clear()

		input("Processing complete! Press the 'enter' key to continue...")

	def save(self):
		self.filename = self.data["Filename"]
		with open(f"{self.filename}.json", "w+") as f:
			json.dump(self.data, f)

	def save_load(self):
		
		while True:

			click.clear()
			
			try:
				x = input("What is the name of the file you would like to load?\n\nInput:\t")

				with open(f"{x}.json") as f:
					self.data = json.load(f)

				click.clear()

				print("\nAccount has been successfully loaded, your game data is up to date and you are ready to continue.\n")
				break

			except FileNotFoundError:
				print("\n\nThat is an incorrect file name, please try again.")
				time.sleep(2)
		
	def load_save(self):
		
		while True:

			click.clear()
			
			try:
				x = input("Please confirm the name of your save file.\n\nInput:\t")

				with open(f"{x}.json") as f:
					self.data = json.load(f)

				click.clear()

				print("\nAccount has been successfully saved, your game data is up to date and you are ready to continue.\n")
				break

			except FileNotFoundError:
				print("\n\nPlease try again.")
				time.sleep(2)

class hero_character(opening_sequence):

	def __init__(self, name, age, supertype, filename):
		super().__init__(name, age, supertype, filename)
		self.hero_attributes = {"Power": 0, "Attacks": 0, "Defence": 0, "Health": 50, "Popularity": 0, "Super Move": 0, "Level": 0}
		self.level_modifiers = [["Level 1", 1], ["Level 2", 1.5], ["Level 3", 2], ["Level 4", 3], ["Level 5", 5, "Super Move Unlock"]]
		self.attacks = [["Quick Punches", 5], ["Ground Slam", 10], ["Normal Punch", 2], ["Flying heel kick", 5]]
		self.defences = [["Quick dodge", 5], ["Block", 2] ,["Invisible dodge", 10], ["Air dodge", 5], ["Hardened skin", 10]]

	def printthing(self):
		print(self.data)
	
	def hero_attributes_assignment(self):

		if self.data["Supertype"] == 1:
			self.data["Power"] = "Super speed"
			self.data["Attacks"] = self.attacks[0]
			self.data["Defence"] = self.defences[0]
		elif self.data["Supertype"] == 2:
			self.data["Power"] = "Super strength"
			self.data["Attacks"] = self.attacks[1]
			self.data["Defence"] = self.defences[1]
		elif self.data["Supertype"] == 3:
			self.data["Power"] = "Invisibility"
			self.data["Attacks"] = self.attacks[2]
			self.data["Defence"] = self.defences[2]
		elif self.data["Supertype"] == 4:
			self.data["Power"] = "Levitation/flight"
			self.data["Attacks"] = self.attacks[3]
			self.data["Defence"] = self.defences[3]
		elif self.data["Supertype"] == 5:
			self.data["Power"] = "Impenetrability"
			self.data["Attacks"] = self.attacks[2]
			self.data["Defence"] = self.defences[4]

		self.data["Level"] = self.level_modifiers[0]
	
def fight(self, enemy):
	print("An enemy approaches!\n\nI am " + enemy[0] + ".\n\nLeave now or face my wrath!\n\nOk then, if you wish to die!")

	hit = randint(1, 10) 

	if hit <= 3:
		print("Attack missed! 0 damage taken.")
	else:
		print("Attack hit!" + f"")  #Thise is where I stopped programming

enemy1 = ["The Burglar", ["Attack", "Normal Punch", 2], ["Defence", "Block", 2], ["HP", 10]]

enemy2 = ["The Tiger Brothers", ["Attack", "Double kick", 5], ["Defence", "Block", 2], ["HP", 20]]
