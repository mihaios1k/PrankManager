import time
import sys
import random

animation = "|/-\\"
passwords = ["GPl675Y", "Password", "Barsik", "ImCool", "Zinabab", "Qwerty"]

print(" __          ___  __ _   _    _            _    ")
print(" \ \        / (_)/ _(_) | |  | |          | |   ")
print("  \ \  /\  / / _| |_ _  | |__| | __ _  ___| | __")
print("   \ \/  \/ / | |  _| | |  __  |/ _` |/ __| |/ /")
print("    \  /\  /  | | | | | | |  | | (_| | (__|   < ")
print("     \/  \/   |_|_| |_| |_|  |_|\__,_|\___|_|\_\ ")
print("")
print("Hello. Write wifi name")

input("<name>:")

print("Wait ...")

for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)] + "Processing: ")
    sys.stdout.flush()

print(random.choice(passwords))
input()