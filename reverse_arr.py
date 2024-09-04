def reverse_arr(arr):
    # return arr[::-1]
    n=len(arr)-1
    temp=0
    for i in range(n):
        if i<=n:
            temp = arr[i]
            arr[i] = arr[n]
            arr[n] = temp
            n-=1
    return arr
print(reverse_arr([5,4,3,2,1]))