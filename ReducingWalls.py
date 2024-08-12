def ReducingWalls (arr, n, k) :
    count=0
    for i in range(n-1):
        if arr[i]>k:
            count=count+1
    return count

print(ReducingWalls([2,6,4,8,1,6],6,4))