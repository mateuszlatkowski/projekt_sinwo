import math

class Euclidean:
    
    def __init__(self):
        self.algorithm_name = "Euclidean Algorithm"
    
    def executes(self, a, b):
        '''Method for computing the greatest common divisor of two numbers (a, b)'''
        while(a!=b):    
            if(a>b):
                a -= b
            else:
                b -= a
        return a
    
    def start(self):
        '''Method gather arguments and send them to execute alghoritm'''
        a = int(input('a: '))
        b = int(input('b: '))
        return self.executes(a, b)
    
    def __repr__(self):
        return self.algorithm_name
    
    def __str__(self):
        return self.__repr__()


class LCM:
    
    def __init__(self):
        self.algorithm_name = "Least Common Multiply"
 
    def executes(self, a, b):
        """Returns the smallest positive integer that is divisible by both a and b"""
        Euclidean_tmp = Euclidean()
        return (a / Euclidean_tmp.executes(a, b)) * b

    def start(self):
        '''Method gather arguments and send them to execute alghoritm'''
        a = int(input('a: '))
        b = int(input('b: '))
        return self.executes(a, b)
    
    def __repr__(self):
        return self.algorithm_name
    
    def __str__(self):
        return self.__repr__()

    
class Fibonacci:
    
    def __init__(self):
        self.algorithm_name = "Fibonacci Number"
 
    def executes(self, N):
        """Every number after the first two is the sum of the two preceding ones"""
        first = (0, 1)
        a, b = first
        number = [0]
        while (N + 1) > 1:
            number.append(b)
            a, b = b, (a + b)
            N -= 1
        return number

    def start(self):
        '''Method gather arguments and send them to execute alghoritm'''
        N = int(input('Number: '))
        return self.executes(N)
    
    def __repr__(self):
        return self.algorithm_name
    
    def __str__(self):
        return self.__repr__()


class Quadratic_formula:
    
    def __init__(self):
        self.algorithm_name = "Quadratic formula"
 
    def executes(self, a, b, c):
        """Quadratic formula solving algorithm"""
        delta = (((b)**2 - 4*a*c)**0.5)
        
        if type(delta) is complex: 
            zeros = None
        elif delta > 0: 
            zeros = ((-b - delta)/(2*a), (-b + delta)/(2*a))
        elif delta == 0: 
            zeros = ((-b)/(2*a))
        
        return zeros

    def start(self):
        '''Method gather arguments and send them to execute alghoritm'''
        a = int(input('a: '))
        b = int(input('b: '))
        c = int(input('c: '))
        return self.executes(a, b, c)
    
    def __repr__(self):
        return self.algorithm_name
    
    def __str__(self):
        return self.__repr__()
    

class Hanoi:
    
    def __init__(self):
        self.algorithm_name = "Hanoi Tower"
        self.steps = 0

    def executes(self, N, z='A', na='C', przez='B'):
        """Conut hanoi tower steps for N pillars"""
        if N == 1:
            self.steps += 1
            #print (z, "->", na) 
            return
        
        self.executes(N - 1, z=z, na=przez, przez=na)
        self.executes(1, z=z, na=na, przez=przez)
        self.executes(N - 1, z=przez, na=na, przez=z)
        return self.steps
        
    def start(self):
        '''Method gather arguments and send them to execute alghoritm'''
        N = int(input('Tower Heigh: '))
        return self.executes(N)
    
    def __repr__(self):
        return self.algorithm_name
    
    def __str__(self):
        return self.__repr__()
    

class FermatFactorization:
    
    def __init__(self):
        self.name = "Fermat Algorithm"
        
    def executes(self, N):
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

    def start(self):
        '''Method gather arguments and send them to execute alghoritm'''
        N = int(input('Number: '))
        return self.executes(N)
    
    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.__repr__()
    

class BubbleSort:
    
    def __init__(self):
        self.name = "Bubble Sort"
        
    def executes(self, data):
        """Bubble sort algorithm"""
        for i in range(len(data)-1, 1, -1):
            for j in range(0, i):
                if data[j] >= data[j+1]:
                    data[j+1], data[j] = data[j], data[j+1]
        return data
    
    def start(self):
        '''Method gather arguments and send them to execute alghoritm'''
        N = int(input('Enter table length: '))
        data = []
        for i in range(0, N):
            x = int(input('Number: '+str(i+1)+' '))
            data.append(x)
            
        return self.executes(data)
    
    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.__repr__()