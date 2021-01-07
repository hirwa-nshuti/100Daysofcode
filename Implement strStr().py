class Str:
    def strStr(self, haystack, needle) :

        if not needle:
            return 0
        if not haystack:
            return -1
        if len(needle)>len(haystack):
            return -1
        while needle and haystack:
            if needle in haystack:
                return haystack.index(needle)
            else:
                return -1
            break

if __name__ == "__main__":
    a="Hello"
    b="ll"
    c="abbbaba"
    d="bbb"
    print(Str().strStr(a,b))
    print(Str().strStr(c,d))