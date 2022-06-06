# Function for swapping two number using XOR:
def swap_two_num(a,b):                     # input is two number a and b.

# Operation of XOR on a and b:
    a = a ^ b
    b = a ^ b
    a = a ^ b

    return(a, b)                            # return swap value of a and b.

# Example:
print(swap_two_num(12, 25))   