def findmedian(arr):
    arr.sort()
    if len(arr)%2!=0:
        n=len(arr)//2
        return arr[n]
    else:
        n=len(arr)
        s=(arr[n // 2 - 1] + arr[n // 2]) / 2
        return s

print(findmedian([1, 2, 3, 4, 5, 6, 8, 9]))