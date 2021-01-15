
#Importing the deque Library
from collections import deque  
#ACTUAL CODE
class Ugly:
    def nthUglyNumber(self, n: int) -> int:
        if n==1:
                return 1
        else:
            u2, u3, u5 = deque([2]), deque([3]), deque([5])
            for _ in range(n-1):

                next_num = min(u2[0],u3[0],u5[0])
                if next_num==u2[0]:
                    u2.popleft()
                if next_num==u3[0]:
                    u3.popleft()
                if next_num==u5[0]:
                    u5.popleft()
                u2.append(next_num*2)
                u3.append(next_num*3)
                u5.append(next_num*5)
            return next_num

print(Ugly().nthUglyNumber(10))
print(Ugly().nthUglyNumber(1))
print(Ugly().nthUglyNumber(18))
print(Ugly().nthUglyNumber(12))
print(Ugly().nthUglyNumber(123))