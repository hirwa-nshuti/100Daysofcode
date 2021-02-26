'''
Given two sequences pushed and popped with distinct
 values, return true if and only if this could have
  been the result of a sequence of push and pop operations on 
an initially empty stack.
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

'''
class Stack:
    def validateStackSequences(self, pushed, popped):
        if len(pushed)!=len(popped):
            return False
        if pushed == popped:
            return True

        index_push = 0
        index_pop = 0
        while pushed and index_push < len(pushed):
            pushTop = pushed[index_push]
            popTop = popped[index_pop]

            if pushTop == popTop:
                pushed.pop(index_push)
                index_push -= 1
                index_pop += 1
            else:
                index_push += 1

            if pushed and index_push < 0:
                index_push += 1

        return len(pushed)==0
pushed=[1,2,3,4,5]
popped=[4,5,3,2,1]
print(Stack().validateStackSequences(pushed,popped))