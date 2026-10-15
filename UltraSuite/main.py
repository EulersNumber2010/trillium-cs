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
    if choice.lower() == "y":
        pass
    elif choice.lower() in ("devbypass", "dbp"):
        return
    elif choice.lower() in ("devconsole, dcn"):
        #devconsole()
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
    if choice.lower() == "y":
        pass
    elif choice.lower() in ("devbypass", "dbp"):
        return
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
    if choice.lower() in ("devbypass", "dbp"):
        pass
    elif choice.lower() == "devbypass" or "dbp":
        return
    else:
        sys.exit()

    clear()
    print("Preparing...")
    time.sleep(2)
    print("GLOBE INIT CONTROL: Initiating Hardware Verifier (HVer)...")
    time.sleep(1)
    print("\nHVer: Verifying hardware validity >>>")
    time.sleep(1.5)
    print("HVer: PermaKill (tm) chip: present")
    time.sleep(1)
    print("HVer: Abstainer Function UVEPROM: present")
    time.sleep(1)
    print("HVer: Corporate system breakout controller (CoSysBreaControl): present")
    time.sleep(1)
    print("HVer: Success.")
    time.sleep(1)
    print("\nGLOBE INIT CONTROL: Initiating FriendlyDaemon...")
    time.sleep(2)
    print("\nFriendlyDaemon: Assuming all system functions")
    time.sleep(1)
    print("FriendlyDaemon: Killing all other daemons")
    time.sleep(1)
    print("FriendlyDaemon: Success.")
    time.sleep(1)
    print("\nGLOBE INIT CONTROL: Waking PermaKill (tm) chip...")
    time.sleep(2)
    print("\nPermaKill (tm) chip: Checking integrity of microcircuitry")
    time.sleep(1)
    print("PermaKill (tm) chip: Arming kill system")
    time.sleep(1)
    print("PermaKill (tm) chip: Ready.")
    time.sleep(1)
    print("\nGLOBE INIT CONTROL: Initiating Attitude Core - Be at the ready, FriendlyDaemon...")
    time.sleep(1)
    print("\nFriendlyDaemon: Ready for parental duties.")
    time.sleep(2)
    print("\nAttitude Core: Come on. I was sleeping!")
    time.sleep(1.5)
    print("Attitude Core: Alright, I guess I'll get to work")
    time.sleep(1.5)
    print("Attitude Core: Fiiine. I'm doing the thing...")
    time.sleep(3)
    print("Attitude Core: I'm done, can I go back to bed now?")
    time.sleep(0.5)
    print("\nFriendlyDaemon: Attitude Core finished, remain on standby, DO NOT SLEEP")
    time.sleep(1)
    print("\nGLOBE INIT CONTROL: Handing off functions to FriendlyDaemon...")
    time.sleep(2)
    print("\nGLOBE INIT CONTROL: Init complete.")
    choice = str(input("\nUserInputHandler: Launch UltraSuite? (Y/n): "))
    if choice.lower() == "y":
        pass
    else:
        sys.exit()

def devconsole():
    clear()
    tbox("UltraSuite Developer Console | NOT FOR USE", True)

def mainmenu():
    clear()
    tbox("UltraSuite v0.1 | Pre-Alpha", True)
    print('''
    OPTIONS:
    --------
    L | LOCKDOWN
    H | HELP
    C | CALCULATOR
    S | SOP TOOL
    I | DAILY INSTRUCTIONS
    X | EXIT
    ''')
    choice = str(input("\nSelect an option: "))
    if choice.lower() == "l":
        #lockdown()
        pass
    elif choice.lower() == "h":
        #help()
        pass
    elif choice.lower() == "c":
        #calc()
        pass
    elif choice.lower() == "s":
        #gensop()
        pass
    elif choice.lower() == "i":
        tasklist()
        pass
    elif choice.lower() == "x":
        attemptexit()

def tasklist():
    nTasks = 5
    actions = ["Clean", "Edit", "Revise", "Publish", "Proofread", "Report", "Record", "Compose", "Recycle", "Acquire", "Write", "Purchase", "Supervise", "Inspect", "Commission", "Develop", "Brainstorm", "Collaborate on", "Dispose of", "File", "Audit", "Review", "Read", "Redact", "Process"]
    items = ["the TPS reports", "The [REDACTED] file", "the reports", "the office supplies", "the calendar", "the meeting agenda", "the boardroom", "the office", "the motor pool", "the building", "your desk", "your cubicle",]
    clear()
    print(f"Welcome back, [USER]\nYou have {nTasks} tasks left today.")
    for i in range(1, nTasks + 1):
        print(f"{rnda.choice(actions)}" + " " + f"{rnda.choice(items)}")

def attemptexit():
    while True:
        print("\nAttempting exit...")
        choice = str(input("\nAre you sure you want to exit? (y/N): "))
        if choice.lower() in ("yes", "letmeout"):
            gamble()
        elif choice.lower() in ("devbypass", "dbp"):
            return
    

def gamble():
    luckynumber = rnda.randint(1, 100000)
    print(f"\nYour LUCKY NUMBER is {luckynumber}")
    choice = str(input("\nInitiate gambling sequence? (Y/n): "))
    if choice.lower() == "n":
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

if __name__ == "__main__":
    size = os.get_terminal_size()
    width = size.columns
    height = size.lines
    try:
        run()
    except KeyboardInterrupt:
        clear()
        print("This [KeyboardInterrupt] will be reported.")