
# coding: utf-8

# In[ ]:

import math

class EuclideanAlgorithm:
    
    def __init__(self):
        self.name = "Algorytm Euklidesa"
        
    def NWD(self, a, b):
        """Is an efficient method for computing the greatest common divisor of two numbers (a, b)"""
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a
    
    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.__repr__()


class LeastCommonMultiple(EuclideanAlgorithm):
    
    def __init__(self):
        self.nazwa = "Najwieksza Wspolna Wielokrotnosc"
        
    def NWW(self, a, b):
        """Is the smallest positive integer that is divisible by both a and b"""
        nww = (a / self.NWD(a, b)) * b
        return nww
    
    def __repr__(self):
        return self.nazwa
    
    def __str__(self):
        return self.__repr__()

    
class klasa3:
    
    def __init__(self):
        self.nazwa_funkcji = "funkcja3"
    
    def __repr__(self):
        return "test klasy3"
    
    def __str__(self):
        return self.__repr__()

