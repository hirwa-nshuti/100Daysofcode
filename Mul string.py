"""Given two non-negative integers num1 and num2 represented as 
strings, 
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or 
convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
"""
def multiply(num1, num2):
    n1 = len(num1) 
    n2 =len(num2)
    if num1[0]=="0" or num2[0]=="0":
        return "0"
    dig = [0] * (n1 + n2)
    for i in reversed(range(n1)):
        for j in reversed(range(n2)):
            prod = dig[i+j + 1] + (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
            dig[i+j] += prod // 10
            dig[i+j + 1] = prod % 10
    res=""
    for d in dig:
        if not res and d == 0: 
            continue
        res+= str(d)
    return res
if __name__=="__main__":
    a,b="432","231"
    c,d="0","2563"
    e,f ="3","4"    
    print("The product of A and B is: \n",multiply(a,b))
    print("The product of C and D is: \n",multiply(c,d))
    print("The product of E and F is: \n",multiply(e,f))