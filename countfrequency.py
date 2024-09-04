def countfrequency(arr):
    d={}
    for i in arr:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
    return d
print(countfrequency([10,5,10,15,10,5]))
print(countfrequency([2,2,3,4,4,2]))