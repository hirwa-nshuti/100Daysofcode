#Python code to specify if a given integer is Palindrome

def isPalindrome(self,x):
    x_string= str(x)
    x_string_reversed=''.join(reversed(x_string))

    if x_string == x_string_reversed:
        return True
    else:
        return False

x=input()