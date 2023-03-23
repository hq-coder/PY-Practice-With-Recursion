# Write code for algorithm 3 below

def fibonacci(n):
    if n <= 0:
        return None 
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibo_22 = fibonacci(22)
print(fibo_22)