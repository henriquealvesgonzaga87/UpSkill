import random

for c in range(128, 256):
    print("%c" % c, end='')

def for1 ():
    print("[------------")
    print("[           |")
    print("[     0     ]")
    print("[           ]")
    print("[-----------]")
    return "For again press Enter"
def for2 ():
    print("[-----------]")
    print("[           ]")
    print("[   0   0   ]")
    print("[           ]")
    print("[-----------]")
    return "For again press Enter"
def for3 ():
    print("[-----------]")
    print("[     0     ]")
    print("[     0     ]")
    print("[     0     ]")
    print("[-----------]")
    return "For again press Enter"
def for4 ():
    print("[-----------]")
    print("[   0   0   ]")
    print("[           ]")
    print("[   0   0   ]")
    print("[-----------]")
    return "For again press Enter"
def for5 ():
    print("[-----------]")
    print("[   0   0   ]")
    print("[     0     ]")
    print("[   0   0   ]")
    print("[-----------]")
    return "For again press Enter"
def for6 ():
    print("[-----------]")
    print("[   0   0   ]")
    print("[   0   0   ]")
    print("[   0   0   ]")
    print("[-----------]")
    return "For again press Enter"
inp=""
while inp =="":
    random_no=random.randint(1,6)
    if random_no==1:
        for1()
    elif random_no==2:
        for2()
    elif random_no==3:
        for3()
    elif random_no==4:
        for4()
    elif random_no==5:
        for5()
    elif random_no==6:
        for6()
    inp=input()