import time
import sys

animation = "|/-\\"

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
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("Password: GFpD765y")
input()