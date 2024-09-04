def removeduplicates(arr):
    # return list(set(arr))
    lst=[]
    for i in arr:
        if i not in lst:
            lst.append(i)
    return lst
print(removeduplicates([2,3,1,9,3,1,3,9]))