def find_smallest_arr(arr):
    # arr.sort()
    # return arr[0]

    # min=arr[0]
    # for i in range(len(arr)):
    #     if arr[i]<min:
    #         min=arr[i]
    # return min
    
    return min(arr)

print(find_smallest_arr([8,10,5,7,9]))