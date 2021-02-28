from heapq import heappush,heappop
from collections import defaultdict
class FreqStack: 

    def __init__(self):
        self.map = defaultdict(int)
        self.heap = []
        self.ctr = 0

    def push(self, x: int) -> None:
        self.map[x] += 1
        heappush(self.heap, (-self.map[x], -self.ctr, x))
        self.ctr += 1

    def pop(self) -> int:
        freq, ctr, x = heappop(self.heap)
        self.map[x] -= 1
        return x

# Your FreqStack object will be instantiated and called as such:
if __name__=="__main__":
    obj = FreqStack()
    obj.push("FreqStack")
    obj.push("push")
    obj.push("push")
    obj.push("push")
    obj.push("push")
    obj.push("push")
    obj.push("push")
    obj.push("pop")
    obj.push("pop")
    obj.push("pop")
    obj.push("pop")
    obj.push(0)
    obj.push(5)
    obj.push(7)
    obj.push(4)
    obj.push(5)
    obj.push(0)
    obj.push(0)
    obj.push(0)
    obj.push(0)
    while obj:
        param_2 = obj.pop()
        print(param_2)