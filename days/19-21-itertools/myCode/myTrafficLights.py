import time
import itertools
import random

lights = 'green yellow red'
lightNames = lights.split()
light_gen = itertools.cycle(lightNames)
while True:
    currentLight = next(light_gen)
    print(currentLight,end="\r")
    if currentLight == lightNames[1]:
        time.sleep(1)
    else:
        time.sleep(1+random.random()*3)
    print("",end="\033[K")

