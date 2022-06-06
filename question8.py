# Function for finding sum of digits of a string:
def sum_int_str(in_str):                              # input is a string.
    emp_str = ""                                      # Declare a empty string.
    sum = 0

# for loop for checking which element is digit and then add into empty string:
    for m in in_str:
        if m.isdigit():
            emp_str += m


# for loop for summtion of digit:   
    for i in range(int(len(emp_str))):
        sum += int(emp_str[i])        

    return sum                                        # return summation of digit.

# Example:
print(sum_int_str("h2015wa73r"))
