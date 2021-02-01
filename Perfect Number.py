'''A perfect number is a positive integer 
that is equal to the sum of its positive divisors, 
excluding the number itself. A divisor of an 
integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect 
number, otherwise return false.'''

from math import sqrt
class Perfect:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False
        out = [1]
        for i in range(2,int(sqrt(num))+1):
            if num%i==0:
                out.append(num//i)
                out.append(i)
        return sum(out)==num

if __name__=="__main__":
    a=28
    b=2
    c=8128
    print(Perfect().checkPerfectNumber(a))
    print(Perfect().checkPerfectNumber(b))
    print(Perfect().checkPerfectNumber(c))