
class Power:
    def myPow(self,x, n):
        if n<0:
            x = 1/x
            n = abs(n)
        ex = 1
        while n > 0:
            if n%2 == 1:
                ex *= x
            x *= x
            n //= 2
        return ex
    

a=int(input())
b=int(input())

print(Power().myPow(a,b))
            
        