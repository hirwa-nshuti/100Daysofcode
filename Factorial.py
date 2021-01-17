class Factorial:
    def factorial(self,n):
        if n<0:
            return 0
        elif n==0 or n==1:
            return 1
        else:
            fact=1
            while(n):
                fact=fact*n
                n-=1
            return fact

print(Factorial().factorial(4))
print(Factorial().factorial(7))
print(Factorial().factorial(5))