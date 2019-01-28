from algos import algorithms
import pytest

def test_Euclidean_1():
    assert algorithms.Euclidean().executes(2310, 525) == 105

def test_Euclidean_zeros():
    assert algorithms.Euclidean().executes(0, 0) == 0

def test_Euclidean_same():
    assert algorithms.Euclidean().executes(2000, 2000) == 2000

def test_LCM():
    assert algorithms.LCM().executes(2310, 525) == 11550

def test_LCM1():
    assert algorithms.LCM().executes(4, 4) == 4.0

def test_LCM2():
    assert algorithms.LCM().executes(525, 525) == 525

def test_Fibonacci():
    assert algorithms.Fibonacci().executes(5) == [0, 1, 1, 2, 3, 5]

def test_Fibonacci2():
    assert algorithms.Fibonacci().executes(2) == [0, 1, 1]

def test_Fibonacci3():
    assert algorithms.Fibonacci().executes(0) == [0]

def test_Quadratic_formula():
    assert algorithms.Quadratic_formula().executes(1, 2, -3) == (-3.0, 1.0)

def test_Quadratic_formula():
    assert algorithms.Quadratic_formula().executes(10, 4, 2) == None

def test_Quadratic_formula():
    assert algorithms.Quadratic_formula().executes(4, 2, -10) == (-1.8507810593582121, 1.3507810593582121)

def test_FermatFactorization():
    assert algorithms.FermatFactorization().executes(855855) == [3, 3, 5, 7, 11, 13, 19]

def test_FermatFactorization2():
    assert algorithms.FermatFactorization().executes(100) == [2, 2, 2, 5, 5, 5.0]

def test_FermatFactorizationZero():
    assert algorithms.FermatFactorization().executes(0) == 0

def test_Hanoi():
    assert algorithms.Hanoi().executes(10) == 1023

def test_Hanoi2():
    assert algorithms.Hanoi().executes(1) == None

def test_Hanoi3():
    assert algorithms.Hanoi().executes(4) == 15

def test_BubbleSort():
    assert algorithms.BubbleSort().executes([5, 3, 8, 7, 0, 1, 9, 2, 4, 10, 6]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_BubbleSort2():
    assert algorithms.BubbleSort().executes([1, 2, 3]) == [1, 2, 3]

def test_BubbleSort3():
    assert algorithms.BubbleSort().executes([1]) == [1]