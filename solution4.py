# Write code for algorithm 4 below

def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)


result = power(2, 4)
print(result)