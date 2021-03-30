"""
Like when you own a store and you want to sort customers based on how
much they paid products
The reason why it is called bubble sort is because bubble in water can come
from bottom to top and the highs value in an array can be moved to the last index 
of our array
"""

#Bubble Sort Implementation

def bubble_sort(elements):
    size = len(elements)

    is_sorted = False
    for i in range(size-1):
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                elements[j],elements[j+1] = elements[j+1],elements[j]
                is_sorted = True
        if not is_sorted:
            break    
def bubble_sort_ex(elements,key=None):
    size = len(elements)
    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            a = elements[j][key]
            b = elements[j+1][key]
            if a > b:
                elements[j],elements[j+1] = elements[j+1],elements[j]
                swapped = True

        if not swapped:
            break    
if __name__ == "__main__":
    elements = [5,9,2,1,65,39,97,39,80]
    bubble_sort(elements)

    print(elements)
    el = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    bubble_sort_ex(el,key="transaction_amount")
    print(el)