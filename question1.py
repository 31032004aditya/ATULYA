# Funtion for differnt list class according to input string:
def list_class(list_num, string):         # function takes two parameter first list of numbers and another string.

# Using if elif elif check string name and then according to that return modified list:

    if(string == "asc"):
        list_num.sort()
        ans = list_num

    elif(string == "desc"):
        list_num.sort()
        list_num.reverse()
        ans = list_num

    elif(string == "none"):
        ans = list_num

    return ans                         # return a list of numbers.

# Example:
print(list_class([23,4,15,6,34,2,78,8], "asc"))
print(list_class([23,4,15,6,34,2,78,8], "desc"))
print(list_class([23,4,15,6,34,2,78,8], "none"))