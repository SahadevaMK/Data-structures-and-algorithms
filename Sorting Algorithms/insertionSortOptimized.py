def insertionsort(arr):
    for i in range(1,len(arr)):
        j=i
        while(arr[j-1] > arr[j] and j>0):
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j-=1

arr = [2,3,6,8,9,4,3]
insertionsort(arr)
print(arr)
