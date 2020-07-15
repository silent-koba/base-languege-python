from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = ['red', 'yellow', 'green']

    def running(self):
        с = 1
        for el in cycle(self.__color):
            if с > 6:
                break
            if el in 'red':
                print(el)
                sleep(7)
            elif el in 'yellow':
                print(el)
                sleep(2)
            else:
                print(el)
                sleep(4)
            с += 1


t = TrafficLight()
t.running()