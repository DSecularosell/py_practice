"""
This is test code for github practice

"""
from time import sleep

def do_something(value,time):
    count = 0
    total = 0
    print('This is gonna take a value and multiply it by a time(in hours). Booting up...')
    sleep(4)
    while count <= len(range(0,time)):
        sleep(2)
        total += value
        count += 1
    return total



print(do_something(60, 10))
