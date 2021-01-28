"""You are given two jugs with capacities x and y litres. 
There is an infinite amount of water supply available. 
You need to determine whether it is 
possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have 
z liters of water contained within one or both buckets by the end.

Operations allowed:

    Fill any of the jugs completely with water.
    Empty any of the jugs.
    Pour water from one jug into another till the 
    other jug is completely full or the first jug itself is empty.

Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
"""
class Jug:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        return z == 0 or (x + y >= z and z % self.gcd(x, y) == 0)       
    def gcd(self, x, y):
        if y==0:
            return x
        else:
            return self.gcd(y,x%y)
        
if __name__=="__main__":
    x=3
    y=5
    z=4
    print(Jug().canMeasureWater(x,y,z))