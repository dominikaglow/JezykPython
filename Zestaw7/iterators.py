import itertools
import random

def cyclePrint():
    outputList = itertools.cycle('01')
    for elem in outputList:
        print(elem, end=" ")

def random_choice():
    letters = ["N", "E", "S", "W"]
    while True:
        step = random.choice(letters)
        print(step, end=" ")

def daysOfTheWeek():
    l = list(range(0, 7))
    for elem in itertools.cycle(l):
        print(elem, end=" ")
# cyclePrint()
# random_choice()
daysOfTheWeek()