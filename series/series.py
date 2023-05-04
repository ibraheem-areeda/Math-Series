def fibonacci(n):
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
        return fibonacci(n-1)+fibonacci(n-2)
   
    
    


