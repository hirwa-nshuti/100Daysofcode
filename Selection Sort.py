#Implementing Selection Sort Algorithm

def selection_sort(arr):
    size = len(arr)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1,size):
            if arr[j]< arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i],arr[min_index] = arr[min_index],arr[i]




if __name__ == '__main__':
    tests = [
        [11,9,29,7,2,15,28],
        [],
        [10,8,2,1,0],
        [1,2],
        [20,1920,0,0]
        ]
    for elements in tests:
        selection_sort(elements)
        print(f"Sorted Elements{elements}")