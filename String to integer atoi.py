class StringTointeger:
    def string_to_integer(str: str) -> int:
        str =str.lstrip()
        i=0
        out=""
        if not str:
            return 0
        elif str[0] not in "+-0987654321":
            return 0
        if str[0] in "+-":
            if len(str)==1:
                return 0
            elif str[1].isdigit()==False:
                return 0
        if str[0]=="-":
            sign = -1
        elif str[0]=="+":
            sign = +1
        else:
            sign =1
        str =str.lstrip("-")
        str =str.lstrip("+")

        while i<len(str) and str[i].isdigit():
            out +=str[i]
            i+=1
        int_s=out*sign    
        int_s_with_sign = (int(out))*sign            
        while int_s_with_sign<=-2**31 or int_s_with_sign>=2**31-1:
            if int_s_with_sign<=-2**31:
                return -2**31
            elif int_s_with_sign>=2**31-1:
                return 2**31-1
            else:
                return int_s_with_sign
        return int_s_with_sign
print("original string is -00000546")
print("Conveted string is:\n")
print(StringTointeger.string_to_integer("-00000546"))
print("original string is -45ebg875")
print("Conveted string is:\n")
print(StringTointeger.string_to_integer("-45ebg875"))
print("original string is hirwa123")
print("Conveted string is:\n")
print(StringTointeger.string_to_integer("hirwa123"))
print("original string is 42")
print("Conveted string is:\n")
print(StringTointeger.string_to_integer("42"))
print("original string is 8736355628176")
print("Conveted string is:\n")
print(StringTointeger.string_to_integer("8736355628176"))

