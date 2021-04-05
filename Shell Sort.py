"""
Shell Sort is an Optimization over Insertion Sort

"""
def shell_sort(arr):
    size = len(arr)
    gap = size//2

    while gap > 0:
        for i in range(gap,size):
            anchor = arr[i]
            j = i
            while j>=gap and arr[j-gap]>anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2

def foo(arr):
    size = len(arr)
    gap = size // 2
    gap = 3
    for i in range(gap, size):
        anchor = arr[i]
        j = i
        while j>=gap and arr[j-gap]>anchor:
            arr[j] = arr[j-gap]
            j -= gap
        arr[j] = anchor

if __name__ == '__main__':
    tests = [
        [11,9,29,7,2,15,28],
        [],
        [10,8,2,1,0],
        [1,2],
        [20,1920,0,0]
        ]
    for elements in tests:
        shell_sort(elements)
        print(f"Sorted Elements{elements}")