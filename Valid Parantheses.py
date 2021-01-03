class ValidParantheses:
    def isValid(s):
        my_stack=[] 
        parantheses =  {"(": ")", "{": "}", "[": "]"}
        for par in s:
            if par in parantheses:
                my_stack.append(par)
            elif len(my_stack) == 0 or parantheses[my_stack.pop()] != par:
                return False
                break
        return len(my_stack) == 0

a="{]{}}[]))("
b="[][][](){}"
c="{}}}}{}{}()"
d=")("
print(ValidParantheses.isValid(a))
print(ValidParantheses.isValid(b))
print(ValidParantheses.isValid(c))
print(ValidParantheses.isValid(d))