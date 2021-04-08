class Solution:
    def calculate(self, s):
        res, sign, num  = 0, 1, 0
        stack_sign = []  
        stack_sum = [] 
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i<len(s) and s[i].isdigit():
                    num = 10*num+int(s[i])
                    i+=1
                res += sign*num
            else:
                if s[i] in '+-':
                    sign = 1 if s[i]=='+' else -1
                elif s[i] =='(':
                    stack_sign.append(sign)
                    stack_sum.append(res)
                    sign = 1
                    res = 0
                elif s[i] == ')':
                    res = stack_sum.pop()+res* stack_sign.pop()
                i+=1
        return res


if __name__ =="__main__":
    calc = Solution()
    s = "(1+(4+5+2)-3)+(6+8)"

    print(calc.calculate(s))