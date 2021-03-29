import timeit


def linear_search(num_list,num_to_find):
    for index ,elment in enumerate(num_list):
        if elment == num_to_find:
            return index
    return -1


def binary_search(num_list,num_to_find):
    left_index = 0
    right_index = len(num_list)-1
    mid_index = 0

    while left_index < right_index:
        mid_index = (left_index + right_index)//2
        mid_number = num_list[mid_index]
        if mid_number == num_to_find:
            return mid_index
        if mid_number < num_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index-1

    return -1

def binary_search_recursive(num_list,num_to_find,left_index,right_index):
        if right_index < left_index:
            return -1
        mid_index = (left_index + right_index)//2

        if mid_index >= len(num_list) or mid_index < 0:
            return -1

        mid_number = num_list[mid_index]
        if mid_number == num_to_find:
            return mid_index

        if mid_number == num_to_find:
            return mid_index

        if mid_number < num_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index-1

        return binary_search_recursive(num_list,num_find,left_index,right_index)         

if __name__ == "__main__":
    nums_list = [12,15,17,19,21,24,45,67]
    num_find = 24

    index = binary_search_recursive(nums_list,num_find,0,len(nums_list))
    print(f"Number of index is: {index} using Recursive Search")
    
