import time
import sys
import random

animation = "|/-\\"
passwords = ["GPl675Y", "Password", "Barsik", "ImCool", "Zinabab", "Qwerty", "123456", "123456789", "1234567", "12345678", "iloveyou", "111111", "abc123", "1q2w3e4r", "qwertyuiop", "password1"]

print("____   ________  __. __________                                               .___   __                .__   ")
print("\   \ /   /    |/ _| \______   \_____    ______ ________  _  _____________  __| _/ _/  |_  ____   ____ |  |  ")
print(" \   Y   /|      <    |     ___/\__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ |  \   __\/  _ \ /  _ \|  |  ")
print("  \     / |    |  \   |    |     / __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ |   |  | (  <_> |  <_> )  |__")
print("   \___/  |____|__ \  |____|    (____  /____  >____  >  \/\_/ \____/|__|  \____ |   |__|  \____/ \____/|____/")
print("                  \/                 \/     \/     \/                          \/                            ")
print("")
print("Print Vk id")

kok = input("<id>:")

for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)] + "Processing: ")
    sys.stdout.flush()

print(random.choice(passwords))
input()