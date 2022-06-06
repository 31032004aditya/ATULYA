from typing import Counter

# Function for finding odd frequency of element:
def oddElement(arr):
    n = int(len(arr))
    count_map = Counter(arr)           # Using counter fun find frequency of each element of arr. 

# for loop for finding odd frequency element:
    for i in range(n):
        if (count_map[arr[i]] % 2 != 0):
            return arr[i]                      # return odd frequency element.

# Example:
print(oddElement([2,4,3,2,5,3,1,4,2,3,2,3,1]))            