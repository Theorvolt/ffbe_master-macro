########################################################################################
#Property of Theorvolt. Don't skid >:(                                                 #
########################################################################################

import pyautogui, time, os, os.path, shutil, psutil

d = os.getcwd()

os.chdir("..")

o = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))] # Gets all directories in the folder as a tuple

l = 'C:\\Users\\Sai2\\Documents\\Coding\\ffbe-macro\\Buttons'

mc = pyautogui

mc.PAUSE = 0

mc.FAILSAFE = True
    
########################################################################################
#Starts defining different button clicks.                                              #
########################################################################################

def world():
    world = mc.locateOnScreen(l+"\\world.png") #Is located at: (817, 688, 250, 223)    
    print(world)
    world_int = mc.center(world)
    print(world_int)
    mc.click(world_int)

    
def unit():
    unit = mc.locateOnScreen(l+"\\units.png")
    returner = mc.locateOnScreen(l+"\\return.png") #Is located at: (1882, 951, 38, 36)
    returner_int = mc.center(returner)
    mc.click(returner_int)#click at (1901, 969)

def nox_back():
    nox_back = mc.locateOnScreen(l+"\\return.png") #Is located at: (1882, 951, 38, 36)
    print(nox_back)
    nx_bk = mc.center(nox_back)
    print(nx_bk)
    mc.click(nx_bk)
    
def nox_home():
    nox_home = mc.locateOnScreen(l+"\\menu.PNG")
    print(nox_home)
    nx_hm = mc.center(nox_home)
    print(nx_hm)
    mc.click(nx_hm)

def end_session():
    #Detects run out of NRG. TODO
    print("undone")

def grandshelt():
    mc.dragRel(-400,0, duration=3)
    grandshelt = mc.locateOnScreen(l+"\\grandshelt.png")
    print(type(grandshelt))

def do_es():
    no = input("One run or infinite?")
    if no == "one":
        print("undone")
        #yadayada does a loop and once end session is detected, terminates.
    if no == "infinite":
        print("undone")
        #Does the same thing but once at 1 nrg, waits 5 minutes before doing.

def trial():
    world()
    time.sleep(2)
    grandshelt()

def unit1():
    mc.click(792,723)
    
def unit2():
    mc.click(1068,721)
    
def unit3():
    mc.click(784,828)

def unit4():
    mc.click(1062,835)

def unit5():
    mc.click(782, 933)
    
def unit6():
    mc.click(1084,928)

def auto():
    mc.click(719,1041)
    
def allout():
    unit1()
    unit2()
    unit3()
    unit4()
    unit5()
    unit6()


def loop():
    es_loop = mc.locateOnScreen(l+"\\es_exit.png")
    print(es_loop)
    es_lp = mc.center(es_loop)
    print(es_lp)
    mc.click(es_lp)
    mc.moveTo(1917,1060)
    time.sleep(5)
    check1 = mc.locateOnScreen(l+"\\es_exitm.png")
    print(check1)
    if isinstance(check1, tuple) == True:
        mc.click(938,946)
    time.sleep(2)
    mc.click(930,370)
    time.sleep(2)
    mc.click(940,950)
    time.sleep(12)
    print("1")
    unit3()
    unit1()
    time.sleep(12)
    print("2")
    unit3()
    unit1()
    time.sleep(12)
    print("3")
    unit3()
    unit1()
    time.sleep(15)
    #Mission ends around here.
    mc.click(942,946)
    time.sleep(2)
    mc.click(942,946)
    mc.click(950,948)
    mc.click(950,948)
    
    

    
    
        

########################################################################################
#Begins the bot.                                                                       #
########################################################################################

while True:
    userinput = input("What would you like to do today? \n If you don't know what to do, query with Help.  ")

    if userinput == "Help":
        print("")
        print("Available Commands:\n Help - Asks for available commands. \n es - Runs Earth Shrine.\n Abort - Breaks out of the loop.")
        print("")
        time.sleep(1)
    if userinput == "Abort":
        break
    if userinput == "es":
        do_es()
        


