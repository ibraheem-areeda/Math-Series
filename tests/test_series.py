import pytest
from series.series import fibonacci

def test_edge1():
    actual = fibonacci(1) #call the function with the test value
    expected = 1 #put the expected result 
    assert actual == expected  #it will return true or false 

def test_edge2():
    actual = fibonacci(0) 
    expected = 0 
    assert actual == expected  

def test_two():
    actual = fibonacci(2) 
    expected = 1 
    assert actual == expected  

def test_three():
    actual = fibonacci(3) 
    expected = 2 
    assert actual == expected  

def test_four():
    actual = fibonacci(4) 
    expected = 3 
    assert actual == expected  

def test_five():
    actual = fibonacci(5) 
    expected = 5
    assert actual == expected  

def test_five():
    actual = fibonacci(5) 
    expected = 5
    assert actual == expected  

def test_six():
    actual = fibonacci(6) 
    expected = 8
    assert actual == expected  

def test_seven():
    actual = fibonacci(7) 
    expected = 13
    assert actual == expected  

def test_ten():
    actual = fibonacci(10) 
    expected = 55
    assert actual == expected  

def test_eighteen():
    actual = fibonacci(18) 
    expected = 2584
    assert actual == expected  

##################################### lucas ##################################

