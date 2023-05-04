import pytest
from series.series import fibonacci_recursion,lucas_recursion,sum_series


##################################### fibonacci ##################################

def test_fibonacci_edge1():
    actual = fibonacci_recursion(1) #call the function with the test value
    expected = 1 #put the expected result 
    assert actual == expected  #it will return true or false 

def test_fibonacci_edge2():
    actual = fibonacci_recursion(0) 
    expected = 0 
    assert actual == expected  

def test_fibonacci_two():
    actual = fibonacci_recursion(2) 
    expected = 1 
    assert actual == expected  

def test_fibonacci_three():
    actual = fibonacci_recursion(3) 
    expected = 2 
    assert actual == expected  

def test_fibonacci_four():
    actual = fibonacci_recursion(4) 
    expected = 3 
    assert actual == expected  

def test_fibonacci_five():
    actual = fibonacci_recursion(5) 
    expected = 5
    assert actual == expected  

def test_fibonacci_six():
    actual = fibonacci_recursion(6) 
    expected = 8
    assert actual == expected  

def test_fibonacci_seven():
    actual = fibonacci_recursion(7) 
    expected = 13
    assert actual == expected  

def test_fibonacci_ten():
    actual = fibonacci_recursion(10) 
    expected = 55
    assert actual == expected  

def test_fibonacci_eighteen():
    actual = fibonacci_recursion(18) 
    expected = 2584
    assert actual == expected  

##################################### lucas ##################################

def test_lucas_edge1():
    actual = lucas_recursion(1) 
    expected = 1 
    assert actual == expected  

def test_lucas_edge2():
    actual = lucas_recursion(0) 
    expected = 2
    assert actual == expected  

def test_lucas_two():
    actual = lucas_recursion(2) 
    expected = 3 
    assert actual == expected  

def test_lucas_three():
    actual = lucas_recursion(3) 
    expected = 4
    assert actual == expected  

def test_lucas_four():
    actual = lucas_recursion(4) 
    expected = 7
    assert actual == expected  

def test_lucas_five():
    actual = lucas_recursion(5) 
    expected = 11
    assert actual == expected  

def test_lucas_six():
    actual = lucas_recursion(6) 
    expected = 18
    assert actual == expected  

def test_lucas_seven():
    actual = lucas_recursion(7) 
    expected = 29
    assert actual == expected  

def test_lucas_ten():
    actual = lucas_recursion(10) 
    expected = 123 
    assert actual == expected  

def test_lucas_eighteen():
    actual = lucas_recursion(30) 
    expected = 1860498   
    assert actual == expected  

    ##################################### sum_series as default (fibonacci) ##################################

def test_sum_series_as_fibo():
    actual = sum_series(1) 
    expected = 1 
    assert actual == expected  

def test_sum_series_as_fibo():
    actual = sum_series(0) 
    expected = 0 
    assert actual == expected  

def test_sum_series_as_fibo():
    actual = sum_series(2) 
    expected = 1 
    assert actual == expected  

def test_sum_series_as_fibo():
    actual = sum_series(3) 
    expected = 2 
    assert actual == expected  

def test_sum_series_as_fibo():
    actual = sum_series(4) 
    expected = 3 
    assert actual == expected  

def test_sum_series_as_fibo():
    actual = sum_series(5) 
    expected = 5
    assert actual == expected  

def test_sum_series_as_fibo():
    actual = sum_series(6) 
    expected = 8
    assert actual == expected  

def test_sum_series_as_fibo():
    actual = sum_series(7) 
    expected = 13
    assert actual == expected  

def test_sum_series_as_fibo():
    actual = sum_series(10) 
    expected = 55
    assert actual == expected  

def test_sum_series_as_lucas():
    actual = sum_series(18) 
    expected = 2584
    assert actual == expected  

    ##################################### sum_series as lucas  ##################################

def test_sum_series_as_lucas():
    actual = sum_series(1 , 2 , 1) 
    expected = 1 
    assert actual == expected  

def test_sum_series_as_lucas():
    actual = sum_series(0 , 2 , 1) 
    expected = 2 
    assert actual == expected  

def test_sum_series_as_lucas():
    actual = sum_series(2 , 2 , 1) 
    expected = 3 
    assert actual == expected  

def test_sum_series_as_lucas():
    actual = sum_series(3 , 2 , 1) 
    expected = 4 
    assert actual == expected  

def test_sum_series_as_lucas():
    actual = sum_series(4, 2 , 1) 
    expected = 7 
    assert actual == expected  

def test_sum_series_as_lucas():
    actual = sum_series(5, 2 , 1) 
    expected = 11
    assert actual == expected  

def test_sum_series_as_lucas():
    actual = sum_series(6, 2 , 1) 
    expected = 18
    assert actual == expected  

def test_sum_series_as_lucas():
    actual = sum_series(7, 2 , 1) 
    expected = 29
    assert actual == expected  

def test_sum_series_as_lucas():
    actual = sum_series(10, 2 , 1) 
    expected = 123
    assert actual == expected  

def test_sum_series_as_lucas():
    actual = sum_series(30, 2 , 1) 
    expected = 1860498
    assert actual == expected  
                                                                      

                                                                       
                                                                       

