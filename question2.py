# Function for the print last four digit in the form of a string of a credit card number:
def credit_card(card_num):                               # function takes input card number.
    
    str_card_num = str(card_num)                         # convert into string.
    
    if(int(len(str_card_num)) == 16):                    # Check: total no. of digit in card is 16 or not.
        ans = str_card_num[-4:]                          # extract last four digits of string in the form of a string.

        return ans                                       # return value is a string.

    else:
        return("CARD NUMBER ERROR")                      # return value is a string.
        
        
#Example;
print(credit_card(4444444444444444))
print(credit_card(234678466176487))