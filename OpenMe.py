import os
import sys

while True:
	print("  _    _            _    _             __  __                                     ___    ___  ")
	print(" | |  | |          | |  (_)           |  \/  |                                   |__ \  / _ \ ")
	print(" | |__| | __ _  ___| | ___ _ __   __ _| \  / | __ _ _ __   __ _  __ _  ___ _ __     ) || | | |")
	print(" |  __  |/ _` |/ __| |/ / | '_ \ / _` | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|   / / | | | |")
	print(" | |  | | (_| | (__|   <| | | | | (_| | |  | | (_| | | | | (_| | (_| |  __/ |     / /_ | |_| |")
	print(" |_|  |_|\__,_|\___|_|\_\_|_| |_|\__, |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|    |____(_)___/ ")
	print("                                  __/ |                          __/ |                        ")
	print("                                 |___/                          |___/                         ")

	print("1)VK Hack")
	print("2)Instagram Hack")
	kek = input(">:")

	if kek == "1":
		os.system("cls")
		exec(open("Pranks/VK.py").read())

	if kek == "2":
		os.system("cls")
		exec(open("Pranks/Instagram.py").read())

	else:
		print("Error")
		os.system("cls")