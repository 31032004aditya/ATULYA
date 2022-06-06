# Function for counting digits, alphabets and chars of a string:
def count_str(str):                                                      # input is a string.
# initialisation with 0 counting:
    num_digits = 0
    num_alphabets = 0
    num_chars = 0

# for loop for check and count using if elif else:
    for i in str:
        if(i.isdigit() == True):
            num_digits += 1

        elif(i.isalpha() == True):
            num_alphabets += 1

        else:
            num_chars += 1        

# print counting:
    print("number of digits in", str, "is", num_digits)
    print("number of alphabets in", str, "is", num_alphabets)
    print("number of chars in", str, "is", num_chars)

# Example:
count_str("###21JE0***@iitism.ac.in###")

