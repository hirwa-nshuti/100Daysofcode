'''Hercy wants to save money for his first car. He puts money 
in the Leetcode bank every day.
He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, 
he will put in $1 more than the day before. On every subsequent Monday, 
he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the 
Leetcode bank at the end of the nth day.
Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
'''
class Lb:
    def totalMoney(self, n: int) -> int:
        x=0
        carr=n//7
        rem=n%7
        for i in range (carr+1,rem+carr+1):
            x+=i
        for i in range(carr):
            x += 7 * (i + 4)
        return x

print(Lb().totalMoney(10))
print(Lb().totalMoney(100))
print(Lb().totalMoney(8))
print(Lb().totalMoney(3))
print(Lb().totalMoney(900))
print(Lb().totalMoney(128))
                