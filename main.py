# Note: This is not finished, it is only the start of the project.

import sys
import click
import time

sys.path.append("Backend Code")
from Code import opening_sequence, hero_character, main_menu, exit_game, enemy1, enemy2, fight

ops = opening_sequence(0, 0, 0, 0)

h = hero_character(0, 0, 0, 0)
while True:
	x = main_menu()

	if x == 1:
		ops.introduction()
		ops.super_creation()
		ops.save()
		h.load_save()
		h.hero_attributes_assignment()
		h.save()
		break

	elif x == 2:
		h.save_load()
		break

	elif x == 3:
		exit_game()

	else:
		click.clear()
		print("Incorrect Input.")
		time.sleep(2)
