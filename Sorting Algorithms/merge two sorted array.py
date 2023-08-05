def merge(arr1,arr2):
    i=0
    j=0
    m = len(arr1)
    n = len(arr2)
    arr = []
    while((i<m) and (j<n)):
        if (arr1[i]<arr2[j]):
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
    while(i<m):
        arr.append(arr1[i])
        i=i+1
    while(j<n):
        arr.append(arr2[j])
        j=j+1
    return arr

arr1 = [2,3,5,6,9,8]
arr2 = [9,8,6,6,5,6,2]

anr = merge(arr1,arr2)
print(anr)
