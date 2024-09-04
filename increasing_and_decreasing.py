def increasing_decreasing(arr):
    arr.sort()
    increase=arr[:len(arr)//2]
    decrease=arr[len(arr)//2:]
    decrease=decrease[::-1]
    return increase+decrease

print(increasing_decreasing([4,2,8,6,15,5,9,20]))