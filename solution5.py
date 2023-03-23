# Write code for algorithm 5 below

def is_palindrome(s):
    # Convert string to lowercase and remove non-alphanumeric characters
    s = ''.join(c for c in s.lower() if c.isalnum())
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

result = is_palindrome("My Name is hq-Coder!")
print(result)


#bonus

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


result = gcd(10, 15)
print(result)