# Function for finding GCD of two number in time complexity O(log(min(a,b))):
def euclid_gcd(a, b):                         # input is two num a and b.
# swapiing of two number if a<b:
    if(a<b):
        a,b = b,a

    if(b==0):
        return a

    else:
        return euclid_gcd(b, a%b)          

# Example:
print(euclid_gcd(64, 36))  
print(euclid_gcd(0, 36)) 