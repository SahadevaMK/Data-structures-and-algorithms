arr = [1,3,6,9,5,4,2,3]

def bubbleSort(customArr):
    for i in range(len(customArr)-1):
        for j in range(len(customArr)-1):
            if customArr[j] > customArr[j+1]:
                customArr[j] , customArr[j+1]  = customArr[j+1] , customArr[j]

    print(customArr)
    
bubbleSort(arr)
