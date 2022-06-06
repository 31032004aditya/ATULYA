# Function for checking string is palindrome or not:
def palindrome(str):                                # input is string.

    reverse = str[::-1]                             # reverse the input string.

    if(str == reverse):                             # Check str and reverse string are same or not.
        print(str,"is a palindrome")  

    else:
        print(str,"is not a palindrome")  
            

# Example:
palindrome("123321") 
palindrome("INDIA")
palindrome("MALAYALAM")
palindrome("ROBOISM")

   