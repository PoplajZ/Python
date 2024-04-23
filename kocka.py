#!/usr/bin/env python3
#Oliver Slimák

import random

class Kostka:

    def __init__(self, steny):
        self.__pocet_sten = steny

    def __str__(self):
        return f"kostka s {self.__pocet_sten} stěnami"

    def hod(self):
        return random.randint(1,self.__pocet_sten)

    def GetPocetSten(self):
        return self.__pocet_sten

k1 = Kostka(69)
print(k1)
print(k1.GetPocetSten())
print(k1.hod())
