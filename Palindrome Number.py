#Python code to specify if a given integer is Palindrome

def isPalindrome(x):
    #converting our integer into a string
    x_string= str(x)
    
    #reversing the string obtained
    x_string_reversed=''.join(reversed(x_string))

    #checking if the reversed string is the same as the original one
    if x_string == x_string_reversed:
        return True
    else:
        return False

integer=input("Enter the integer ")
print(isPalindrome(integer))