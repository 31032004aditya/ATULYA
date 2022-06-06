# Function for doubled the each element of a string and then return: 
def str_doubled(in_str):                 # function takes a string as input.
    doubled = ''                         # define doubled as empty string.
        
# for loop for extract each element and then store into its 2 times into doubled string:
    for i in in_str:
        doubled += i*2    
    
    return doubled                        # return a string.

# Example:
print(str_doubled("123a!"))