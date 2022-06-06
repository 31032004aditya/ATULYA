# Function for sorted a string:
def sorted_str(str):                             # input is a string.
    ascii_lst = []                               # Declare a lst for ascii val of each element of string.
    out_str = ''                                 # Declare a empty string.

# for loop for appending ascii value of each element of a string into list: 
    for i in str:
        ascii_lst.append(ord(i))

    ascii_lst.sort()                             # sorting of ascii lst.

# for loop for ascii val converted into char and then add in out_str:
    for j in ascii_lst:
        out_str += chr(j)

    return out_str                               # return a sorted string.

# Example:
print(sorted_str("jhbsvdfg34"))    