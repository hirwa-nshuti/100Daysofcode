class Happy:
    def isHappy(self, n: int) -> bool:
        sums_dict={}
        n=int(n)
        while n:
            if n==1:
                return True
            x=0
            while n!=0:
                mod=n%10
                x=x+mod**2
                n=n//10
            if x in sums_dict.keys():
                return False
            sums_dict[x]=None
            n=x

print(Happy().isHappy(19))
print(Happy().isHappy(1000))
print(Happy().isHappy(38))
print(Happy().isHappy(75))