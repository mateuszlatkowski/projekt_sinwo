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

