'''Given two integers dividend and divisor, divide two integers 
without using multiplication, 
division, and mod operator.
Return the quotient after dividing dividend 
by divisor.

The integer division should truncate toward zero, 
which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

    Assume we are dealing with an environment that could only store integers within the 32-bit 
    signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 
    231 − 1 when the division result overflows.
'''

class Div:
    def divide(self, Dividend: int, divisor: int) -> int:
        x=int(Dividend/divisor)
        if x<=2**31-1:
            return x
        else:
            return (2**31-1)

a=int(input("Enter the Dividend: "))
b=int(input("Enter the divisor: "))


print(Div().divide(a,b))