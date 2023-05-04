def fibonacci_recursion(n):
    '''
    function take 1 argument which is n
    return the nth value in the fibonacci series
    using recursion
    '''
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)
    
def lucas_recursion(n):
    '''
     function take 1 argument which is n
     return the nth value in the lucas series
     using recursion
    '''
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas_recursion(n-2) + lucas_recursion(n-1)
    
def sum_series ( n , start_val1=None , start_val2=None ):
    '''
     function create custom series takes 3 arguments which is
       n (reqiured) as the nth value in the custom series ,
       start_val1 (optinal) which is the value at n=0  ,
       start_val2 (optinal) which is the value at n=1 ,
     return the nth value in the custom series
     using recursion
     if no value passed to the optinal agruments the function will return a fibonacci series
    '''
    if n==0:
        return start_val1 or 0
    elif n==1:
        return start_val2 or 1
    else:
        return sum_series(n-2 ,start_val1,start_val2 ) + sum_series(n-1,start_val1,start_val2)

if __name__ == "__main__": 
    sum_series(5)

   
    
    


