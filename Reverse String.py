#Python code to reverse an input string

def reverse(string):
    string = "".join(reversed(string)) 
    return string 


string = input("Enter Your string: ")

print("The Input STring is: \n", end="")
print(string)
print("The Outcome string will be: \n", end="")
print(reverse(string))
