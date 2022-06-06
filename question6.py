# Function for finding prime number lst in given range:
def prime_num(a, b):               # inputs are two number a and b, which gives range.
    lst = []                       # Declare a list.

# Swap the number if a>b:   
    if(a>b):
        a,b = b,a

    n = b-a+1

# loop for finding prime number and append into lst: 
    for i in range(n):
        count = 0
        if(a+i>0):
            for j in range(a+i):
                if((a+i)%(j+1) == 0):
                    count = count + 1
                
            if(count==2):
                lst.append(a+i)

    
    return lst                        # return prime number list.

# Example:    
print(prime_num(-21, 20))
print(prime_num(1, 20))
print(prime_num(10, 20))
print(prime_num(20, 10))       
