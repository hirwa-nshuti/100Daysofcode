class Valid:
    def isPerfectSquare(self, num: int) -> bool:
        low_num=1
        high_num=num
        
        while low_num<=high_num:
            mid_num=(low_num+high_num)//2

            if mid_num*mid_num>num:
                high_num=mid_num-1
            
            elif mid_num*mid_num==num:
                return True
                
            elif mid_num*mid_num<num:
                low_num=mid_num+1
                
        return False

print(Valid().isPerfectSquare(4))
print(Valid().isPerfectSquare(1576625))

#Another Easy Solution
import math
class Square:
    def perfectSquare(self, num: int) -> bool:
        if num==0 or num==1:
            return True
        while num:
            return(num**.5).is_integer()
print(Square().perfectSquare(4))