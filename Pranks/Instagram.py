import random
import time
import sys

animation = "|/-\\"
passwords = ["GPl675Y", "Password", "Barsik", "ImCool", "Zinabab", "Qwerty", "123456", "123456789", "1234567", "12345678", "iloveyou", "111111", "abc123", "1q2w3e4r", "qwertyuiop", "password1"]

print("  _____           _        _    _          _____ _  __")
print(" |_   _|         | |      | |  | |   /\   / ____| |/ /")
print("   | |  _ __  ___| |_ __ _| |__| |  /  \ | |    | ' / ")
print("   | | | '_ \/ __| __/ _` |  __  | / /\ \| |    |  <  ")
print("  _| |_| | | \__ \ || (_| | |  | |/ ____ \ |____| . \ ")
print(" |_____|_| |_|___/\__\__,_|_|  |_/_/    \_\_____|_|\_\ ")
print("")
print("Hi hacker input insta id")
print("")
input("<id>:")

for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)] + "Processing: ")
    sys.stdout.flush()

print(random.choice(passwords))
input()