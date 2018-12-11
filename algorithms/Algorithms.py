
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
        self.name = "Najwieksza Wspolna Wielokrotnosc"
        
    def NWW(self, a, b):
        """Is the smallest positive integer that is divisible by both a and b"""
        nww = (a / self.NWD(a, b)) * b
        return nww
    
    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.__repr__()

    
class FermatFactorization:
    
    def __init__(self):
        self.name = "Algorytm Fermata"
        
    def fermat(self, N):
        """The factorization method, the distriubtion of the number into prime factors"""
        if N <= 0:
            return 0
    
        i  = 2
        e = math.floor(math.sqrt(N))
        numbers = []
    
        while i <= e:
            if N % i == 0:
                numbers.append(i)
                N /= i
                e = e = math.floor(math.sqrt(N))
            else:
                i += 1
    
        if N > 1: numbers.append(N)
        return numbers
    
    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.__repr__()

