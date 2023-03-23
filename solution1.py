# Write code for algorithm 1 below


def numbers(n):
    if n == 0:  # base case
        print(n)
    else:  # recursive case
        print(n)
        numbers(n-1)


numbers(5)