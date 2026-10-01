###################################################################################################
# COPYRIGHT (C) 2026 GLOBE CORP - ALL RIGHTS RESERVED                                             #
# THE CORPORATION RESERVES THE RIGHT TO TERMINATE ANY UNAUTHORIZED PERSON POSESSING THIS SOFTWARE #
###################################################################################################

import os, subprocess, sys
import random as rnda

def clear():
    subprocess.run(["clear"]) # TODO - Fix for NT

def tbox(text, padded=False):
    print("+" + "-"*(len(text)+(2 if padded else 0)) + "+")
    print(("| " if padded else "|") + text + (" |" if padded else "|"))
    print("+" + "-"*(len(text)+(2 if padded else 0)) + "+")

def mainmenu():
    clear()
    tbox("UltraSuite v0.1 | Pre-Alpha", True)

def attemptexit():
    while True:
      print("\nAttempting exit...")
      choice = str(input("\nAre you sure you want to exit? (y/N):"))
      if choice == "letmeout":
          gamble()

def gamble():
    luckynumber = rnda.randint(1, 100000)
    print(f"\nYour LUCKY NUMBER is {luckynumber}")
    choice = str(input("\nInitiate gambling sequence? (Y/n):"))
    if choice == "n":
        pass
    else:
        while(True):
            luck = rnda.randint(1, 100000)
            if luck == luckynumber:
                print(luck)
                print("*** !!!YOU WON!!! ***")
                sys.exit()
            else:
                print(f"{luck}" + "\nREROLL")

if __name__ == "__main__":
    size = os.get_terminal_size()
    width = size.columns
    height = size.lines
    mainmenu()

    # Corporate-mandated infinite loop
    attemptexit()