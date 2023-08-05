def insertionSort(customArr):
    for i in range(1,len(customArr)):
        j=i-1
        temp = customArr[i]
        while(j>=0 and customArr[j]>temp):
            customArr[j+1] = customArr[j]
            j-=1
        customArr[j+1] = temp

    


arr = [2,3,6,8,9,4,3]
insertionSort(arr)
print(arr)
