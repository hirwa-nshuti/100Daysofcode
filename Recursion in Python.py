def find_sum(n):
    sum = 0
    for i in range (1,n+1):
        sum+=i
    return sum

def find_sum_recursive(n):
    if n == 1:
        return 1
    return n + find_sum_recursive(n-1)

def fibonaci(n):
    if n==0 or n==1:
        return n
    return fibonaci(n-1)+fibonaci(n-2)  

if __name__ == "__main__":
    print(find_sum(8))
    print(find_sum_recursive(8))
    print(fibonaci(34))