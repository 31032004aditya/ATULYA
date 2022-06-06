# Function for performing some mathematical calculation:
def cal(int1, oper, int2):                # function takes three input: integer, operator and integer.
    # Using if elif do many operation:
    if(oper == "+"):
        ans = int1 + int2
    
    elif(oper == "-"):
        ans = int1 - int2

    elif(oper == "*"):
        ans = int1 * int2

    elif(oper == "**"):
        ans = int1 ** int2      

    elif(oper == "/"):
        ans = int1 / int2 

    elif(oper == "//"):
        ans = int1 // int2

    elif(oper == "%"):
        ans = int1 % int2       
    
    return ans                      # ans is return value.

# Example:
print(cal(12, '+', 2))
print(cal(12, '-', 2)) 
print(cal(12, '*', 2))
print(cal(12, '**', 2)) 
print(cal(12, '/', 2))
print(cal(12, '//', 2)) 
print(cal(12, '%', 2))     