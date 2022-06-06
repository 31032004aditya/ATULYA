# Function for finding duplicate number from arr of 100 element:
def duplicate_num(arr_100):                       # input is a array of numbers.
    count = 0
    n = int(len(arr_100))

# Using nested for loop extract element and then compare with rest of them:
    for i in range(n):                            
        for j in range(n):
            if(i!=j):
                if (arr_100[i]==arr_100[j]):
                    ans = arr_100[i]
                    break                           # After finding duplicate number loop is break.
    
    return ans                                      # return duplicate number.

#Example:
print(duplicate_num([12,34,56,7,6,87,34,76]))