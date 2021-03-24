"""
Mostly implemented to Producer Consumer problems
FIFO: First In First Out
Like when you are on a line waiting to catch a bus
you will get your ticket based on when you alived and
first to come will be first to be served
Queues class in Python can be
-List
-collections.deque
queue.LifoQueue
"""
#Implementing a Queue Class in Python
import threading
import time
from collections import deque
class Queue:
    def __init__(self):
        self.obj=deque()
    def enqueue(self,data):
        self.obj.appendleft(data)
    def dequeue(self):
        return self.obj.pop()
    def is_empty(self):
        return len(self.obj)==0
    def size(self):
        return len(self.obj)
    def front(self):
        return self.obj[-1]

#Food Ordering function
take_order = Queue()

def place_orders(orders):
    for order in orders:
        print("Placing order for:",order)
        take_order.enqueue(order)
        time.sleep(0.5)


def serve_orders():
    time.sleep(1)
    while True:
        order = take_order.dequeue()
        print("Now serving: ",order)
        time.sleep(2)
        if take_order.size()==0:
            break

if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_orders, args=(orders,))
    t2 = threading.Thread(target=serve_orders)

    t1.start()
    t2.start()

#Printing Binary numbers between 1 and 10 with 1 ec delay
def put_bin(num):
    bin_num=Queue()
    bin_num.enqueue("1")

    for n in range(num):
        front=bin_num.front()
        print(" ",front)
        bin_num.enqueue(front+"0")
        bin_num.enqueue(front+"1")
        bin_num.dequeue()
if __name__=="__main__":
    put_bin(10)