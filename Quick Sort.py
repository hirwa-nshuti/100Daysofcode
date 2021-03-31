"""
Quick Sort we cna take first elemnt of array and put in middle where left is less than pivot
and the right is greater than pivot
It is also called divide and conquer problem
The method of dividing is called partition
Partition schemes: Hoare Partition, Lomuto Partition
"""
#Quick Sort Implementation
def swap(a,b,arr):
    if a!=b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
def partition(elements,start,end):
    pivot_index = start
    pivot = elements[pivot_index]
    while start < end:
        while start <len(elements) and elements[start] <= pivot:
            start +=1

        while elements[end]>pivot:
            end -=1
        if start<end:
            swap(start,end,elements)
    swap(pivot_index,end,elements)
    return end


def quick_sort(elements,start,end):
    if start<end:
        par_index = partition(elements,start,end)
        quick_sort(elements,start, par_index-1)
        quick_sort(elements,par_index+1,end)



if __name__ == "__main__":
    el = [
        [11,9,29,7,2,15,28],
        [],
        [10,8,2,1,0],
        [1,2],
        [20,1920,0,0]
        ]
    for element in el:
        quick_sort(element,0,len(element)-1)
        print(f"The sorted array: {element}")