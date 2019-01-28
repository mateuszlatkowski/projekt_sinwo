from algos import algorithms
import pytest

def test_Euclidean_1():
    assert algorithms.Euclidean().executes(2310, 525) == 105

def test_LCM():
    assert algorithms.LCM().executes(2310, 525) == 11550

def test_Fibonacci():
    assert algorithms.Fibonacci().executes(5) == [0, 1, 1, 2, 3, 5]

def test_Quadratic_formula():
    assert algorithms.Quadratic_formula().executes(1, 2, -3) == (-3.0, 1.0)

def test_FermatFactorization():
    assert algorithms.FermatFactorization().executes(855855) == [3, 3, 5, 7, 11, 13, 19]

def test_Hanoi():
    assert algorithms.Hanoi().executes(10) == 1023

def test_BubbleSort():
    assert algorithms.BubbleSort().executes([5, 3, 8, 7, 0, 1, 9, 2, 4, 10, 6]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
