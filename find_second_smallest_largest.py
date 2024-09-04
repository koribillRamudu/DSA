def second_smallest_and_largest(arr):
    if len(arr)>1:
        arr.sort()
        return f'Second Smallest {arr[1]}\n Second Largest {arr[-2]}'
    return -1
    # small=float('inf')
    # large=float('-inf')
    # second_small=float('inf')
    # second_large=float('-inf')
    # for i in range(len(arr)):
    #     small = min(small, arr[i])
    #     large = max(large, arr[i])
    # for i in range(len(arr)):
    #     if arr[i] < second_small and arr[i] != small:
    #         second_small = arr[i]
    #     if arr[i] > second_large and arr[i] != large:
    #         second_large = arr[i]
    # return second_small,second_large

print(second_smallest_and_largest([2,3,4,5,6]))