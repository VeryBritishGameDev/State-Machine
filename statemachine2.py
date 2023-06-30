import time
from enum import Enum


class State(Enum):
    ## no cross
    RED_NC = 1
    RED_AMBER_NC = 2
    GREEN_NC = 3
    AMBER_NC = 4
    ## waiting
    RED_C = 5
    RED_AMBER_C = 6
    GREEN_C = 7
    AMBER_C = 8
    #misc
    END = 9
currentstate = State.RED_NC
laststate = 0
import msvcrt


def key_pressed():
    if msvcrt.kbhit():
        key_stroke = msvcrt.getch()
        return key_stroke.decode('utf-8') 
    else:
        return None
    
def mainfunc(printmessage,timewait,nextstate, keyuse, nextstatekey):
    global currentstate
    global start_time
    elapsedtime = time.time() - start_time
    if elapsedtime > 0:
        start_time = time.time() + timewait
        currentstate = nextstate
        print(printmessage)
    if keyuse == 'w':
        currentstate = nextstatekey
    if keyuse == 'q':
        currentstate = State.END
    return currentstate

start_time = time.time()
while True:
    key = key_pressed()
    if currentstate == State.RED_NC:
        mainfunc("traffic red", 3, State.RED_AMBER_NC, key, State.RED_C)
    elif currentstate == State.RED_AMBER_NC:
        mainfunc("traffic red-amber", 1, State.GREEN_NC, key, State.RED_AMBER_C)
    elif currentstate == State.GREEN_NC:
        mainfunc("traffic green", 3, State.AMBER_NC, key, State.GREEN_C)
    elif currentstate == State.AMBER_NC:
        mainfunc("traffic amber", 1, State.RED_NC, key, State.RED_C)
    elif currentstate == State.RED_C:
        mainfunc("traffic red, waiting", 1, State.RED_AMBER_C, key, State.RED_AMBER_C)  
    elif currentstate == State.RED_AMBER_C:
        mainfunc("traffic red-amber, waiting", 1, State.GREEN_C, key, State.GREEN_C) 
    elif currentstate == State.GREEN_C:
        mainfunc("traffic green,waiting", 1, State.AMBER_C, key, State.AMBER_C)
    elif currentstate == State.AMBER_C:
        mainfunc("traffic amber, waiting", 1, State.RED_NC, key, State.RED_NC)
    elif currentstate == State.END:
        break