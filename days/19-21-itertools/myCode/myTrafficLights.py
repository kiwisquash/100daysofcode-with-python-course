import time
import itertools
import random

lights = 'green yellow red'.split()

def delayTime(lightIndex):
    if lightIndex == 1:
        return 1
    else:
        return 1 + random.random()*3

def turnOnLights(lights):
    light_gen = itertools.cycle(lights)
    for color in light_gen:
        print(color,end="\r")
        if color == lights[1]:
            time.sleep(delayTime(1))
        else:
            time.sleep(delayTime(2))
        print("\033[K",end="") # Erase to the end of the line 

if __name__ == "__main__":
    turnOnLights(lights)
