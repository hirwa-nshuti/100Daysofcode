'''On a broken calculator that has a number showing 
on its display, we can perform two operations:

    Double: Multiply the number on the display by 2, or;
    Decrement: Subtract 1 from the number on the display.

Initially, the calculator is displaying the number X.

Return the minimum number of operations needed to 
display the number Y.
Input: X = 2, Y = 3
Output: 2
Explanation: Use double operation and then 
decrement operation {2 -> 4 -> 3}.
'''

def brokenCalc(X, Y):
    out=0
    while Y > X:
        out += 1
        if Y%2:
            Y += 1
        else:
            Y /= 2
    return int(out + X - Y)
if __name__=="__main__":
    a=2
    b=3      
    print(brokenCalc(a,b))