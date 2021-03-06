# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):

    if n == 0 or n == 1:
        
        fibo = n
    
    else:
        
        fibo = fibonacci(n-1) + fibonacci(n-2)
    
    return fibo



print(fibonacci(0))
#>>> 0
print( fibonacci(1))
#>>> 1
print(fibonacci(2))
#>>> 1
print(fibonacci(3))
#>>> 2
print(fibonacci(4))
#>>> 3
print(fibonacci(15))
#>>> 610