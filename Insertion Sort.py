"""
Is a simpmle Sorting Algorithm but not efficient with large lists
"""

#Insertion Sort

def insertion_sort(elements):
    for i in range(1,len(elements)):
        anchor = elements[i]
        j=i-1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
            elements[j+1]=anchor

if __name__ == "__main__":
    el = [
        [11,9,29,7,2,15,28],
        [],
        [10,8,2,1,0],
        [1,2],
        [20,1920,0,0]
        ]
    for element in el:
        insertion_sort(element)
        print(f"The sorted array: {element}")
