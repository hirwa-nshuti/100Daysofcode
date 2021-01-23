class ExcelNum:
    def titleToNumber(self, s: str) -> int:
        out=0
        for i,n in enumerate(s[::-1]):
            out+=(26**i)*(ord(n)-64)
        return out

print(ExcelNum().titleToNumber("A"))
print(ExcelNum().titleToNumber("AFG"))
print(ExcelNum().titleToNumber("AB"))
print(ExcelNum().titleToNumber("MV"))
print(ExcelNum().titleToNumber("ZL"))