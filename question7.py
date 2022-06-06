# Function for finding most frequenct num:
def freq_arr(arr_num):                      # input is a arr of number.
    lst = []                                # Declare a list.
    
    freq_num = set()                        # Declare a set.
    max = 0

# for loop for finding frequency of each element, max_frequency and append into lst:    
    for i in arr_num:
        freq = arr_num.count(i)
        lst.append(freq)
        if (freq>max):
            max = freq

# for loop for finding element which have frequency equal to max_frequency:
    for j in range(int(len(lst))):
        if(lst[j] == max):
            freq_num.add(arr_num[j])

    return freq_num                      # return set of most frequent num.
    
# Example:
print(freq_arr([12,7,4,67,7,89,7,4,7,4,4]))
print(freq_arr([12,7,4,67,7,89,7,4,7,4]))