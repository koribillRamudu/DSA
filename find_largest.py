def find_largestele(arr):
    # return max(arr)

    # arr.sort()
    # return arr[-1]


    m=0
    for i in range(len(arr)):
        if arr[i]>m:
            m=arr[i]
    return m
print(find_largestele([2,5,1,3,0]))