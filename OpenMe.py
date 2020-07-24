import os
import sys

while True:
	print("   _    _            _    _             __  __                                     ____  __  \n  | |  | |          | |  (_)           |  \/  |                                   |___ \/_ | \n  | |__| | __ _  ___| | ___ _ __   __ _| \  / | __ _ _ __   __ _  __ _  ___ _ __    __) || | \n  |  __  |/ _` |/ __| |/ / | '_ \ / _` | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|  |__ < | | \n  | |  | | (_| | (__|   <| | | | | (_| | |  | | (_| | | | | (_| | (_| |  __/ |     ___) || | \n  |_|  |_|\__,_|\___|_|\_\_|_| |_|\__, |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|    |____(_)_| \n                                   __/ |                          __/ |                      \n                                  |___/                          |___/                       ")

	print("1)VK Hack")
	print("2)Instagram Hack")
	print("3)Wifi")
	print("W)What install?")
	kek = input(">:")

	if kek == "1":
		os.system("cls")
		exec(open("Pranks/VK.py").read())

	if kek == "2":
		os.system("cls")
		exec(open("Pranks/Instagram.py").read())

	if kek == "3":
		os.system("cls")
		exec(open("Pranks/Wifi.py").read())

	if kek == "W":
		os.system("cls")
		exec(open("Pranks/What.py").read())

	else:
		print("Error")
		os.system("cls")