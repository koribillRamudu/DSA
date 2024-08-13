def get_min_max(self, arr):
    # return min(arr),max(arr)
    # m=arr[0]
    # mx=0
    # for i in range(len(arr)):
    #     if arr[i]<m:
    #         m=arr[i]
    #     if arr[i]>=mx:
    #         mx=arr[i]
    # return m,mx
    arr.sort()
    return arr[0],arr[-1]