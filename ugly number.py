class Ugly:
    def isUgly(self, num: int) -> bool:
        num=int(num)
        
        while num:
            if num==0:
                return False
            while num%2 ==0:
                num=num/2
            while num%3 ==0:
                num=num/3
                
            while num%5==0:
                num=num/5
                
            if num==1:
                return True
            elif num!=1:
                return False

print(Ugly().isUgly(14))
print(Ugly().isUgly(1))
print(Ugly().isUgly(5))
print(Ugly().isUgly(1928263))
print(Ugly().isUgly(900))