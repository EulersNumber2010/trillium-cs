###################################################################################################
# COPYRIGHT (C) 2026 GLOBE CORP - ALL RIGHTS RESERVED                                             #
# THE CORPORATION RESERVES THE RIGHT TO TERMINATE ANY UNAUTHORIZED PERSON POSESSING THIS SOFTWARE #
###################################################################################################

import os, subprocess, sys
import time
import random as rnda

def clear():
    subprocess.run(["clear"]) # TODO - Fix for NT

def tbox(text, padded=False):
    print("+" + "-"*(len(text)+(2 if padded else 0)) + "+")
    print(("| " if padded else "|") + text + (" |" if padded else "|"))
    print("+" + "-"*(len(text)+(2 if padded else 0)) + "+")

def init():
    clear()
    print('''READ THE FOLLOWING TEXT CAREFULLY:
    \nThis is Ultra-Proprietary software. ANY attempt to use this software without a proper authorization will result in IMMEDIATE TERMINATION regardless of age, fault, and/or relationships to GLOBE CORP.''')
    choice = str(input("Do you accept these terms? (y/N): "))
    if choice == "y":
        pass
    else:
        sys.exit()

    clear()
    print('''READ THE FOLLOWING TEXT CAREFULLY:
    \nIn order to use this software product, you must accept the terms and conditions. To obtain a copy of the terms and conditions [1049 pages], write to
    \nGlobe Corporation Legal Department
    12345 Globe Access Road
    Globe Facilities Center, NY 11011
    \nStandard lead time 28 weeks''')
    choice = str(input("\nDo you accept these terms? (y/N): "))
    if choice == "y":
        pass
    else:
        sys.exit()

    clear()
    print('''READ THE FOLLOWING TEXT CAREFULLY:
    \nIn order to use this software product, you must accept the license agreement. To obtain a copy of the license agreement [1049 pages], write to
    \nGlobe Corporation Licensing Bureau
    12345 Globe Access Road
    Globe Facilities Center, NY 11011
    \nStandard lead time 36 weeks''')
    choice = str(input("\nDo you accept these terms? (y/N): "))
    if choice == "y":
        pass
    else:
        sys.exit()

    clear()
    print("Preparing...")
    time.sleep(2)
    print("GLOBE INIT CONTROL: Initiating Hardware Verifier (HVer)...")
    time.sleep(1)
    print("\nHVer: Verifying hardware validity...")
    time.sleep(1)
    print("HVer: PermaKill (tm) chip: present")
    time.sleep(1)
    print("HVer: Abstainer Function UVEPROM: present")
    time.sleep(1)
    print("HVer: Corporate system breakout controller (CoSysBreaControl): present")
    time.sleep(1)
    print("\nGLOBE INIT CONTROL: Initiating FriendlyDaemon...")
    time.sleep(1)
    print("\nFriendlyDaemon: Assuming all system functions")
    time.sleep(1)
    print("FriendlyDaemon: Killing all other daemons")
    time.sleep(1)
    print("FriendlyDaemon: Waking PermaKill (tm) chip")
    time.sleep(1.5)
    print("\nPermaKill (tm) chip: Activating PermaKill (tm) chip")

    print("\nWelcome")

def mainmenu():
    #clear()
    tbox("UltraSuite v0.1 | Pre-Alpha", True)
    print('''
    OPTIONS:
    --------
    L | LOCKDOWN
    H | HELP
    ''')

def attemptexit():
    while True:
      print("\nAttempting exit...")
      choice = str(input("\nAre you sure you want to exit? (y/N): "))
      if choice == "letmeout":
          gamble()

def gamble():
    luckynumber = rnda.randint(1, 100000)
    print(f"\nYour LUCKY NUMBER is {luckynumber}")
    choice = str(input("\nInitiate gambling sequence? (Y/n): "))
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

def run():
    init()
    mainmenu()

    attemptexit()

if __name__ == "__main__":
    size = os.get_terminal_size()
    width = size.columns
    height = size.lines
    try:
        run()
    except KeyboardInterrupt:
        clear()
        print("This [KeyboardInterrupt] will be reported.")