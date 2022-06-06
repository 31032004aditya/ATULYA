# function of finding duplicate number in time compexity of order n:
def duplicate_n_ord(arr):                    # input is a array of number.
   
    for i in arr:
        if(arr.count(i)==2):                 # using count fun check its duplicate or not.
            return i                         # return duplicate value.
            break                            # After finding duplicate break the loop.


print("duplicate num in arr is", duplicate_n_ord([12,2,45,5,67,4,9,88,65,45,33]))
