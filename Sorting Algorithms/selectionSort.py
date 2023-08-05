def selectionSort(arr):
    for i in range(0,len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            if (arr[j] < arr[min]):
                min = j
        if (min != i):
            arr[i],arr[min] = arr[min],arr[i]

arr = [8,2,3,5,7,9,5]
selectionSort(arr)

print(arr)
