def peakElement(arr, n):
    m=0
    v=0
    for i in range(n):
        if arr[i]>=m:
            m=arr[i]
            v=i
        return v
        n=max(arr)
        return arr.index(n)