def rotatearr(arr,k):
    return arr[k:]+arr[:k]
print(rotatearr([1,2,3,4,5],2))