def partition(arr, lowerbound, upperbound):
    pivot = arr[lowerbound]
    start = lowerbound + 1  # Incremented start index by 1
    end = upperbound

    while start <= end:  # Changed while loop condition to handle edge cases
        while start <= end and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]

    arr[lowerbound], arr[end] = arr[end], arr[lowerbound]
    return end

def quickSort(arr1, lb, ub):
    if lb < ub:
        loc = partition(arr1, lb, ub)
        quickSort(arr1, lb, loc - 1)
        quickSort(arr1, loc + 1, ub)

arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
quickSort(arr, 0, len(arr) - 1)
print(arr)


# def partition(arr,lowerbound,upperbound):
#     pivot = arr[lowerbound]
#     start = lowerbound
#     end = upperbound
    
#     while(start < end):
#         while(arr[start]<=pivot):
#             start+=1
#         while(arr[end]>pivot):
#             end-=1
#         if (start<end):
#             arr[start],arr[end] = arr[end],arr[start]
#     arr[lowerbound],arr[end] = arr[end],arr[lowerbound]
#     return end

# def quickSort(arr,lb,ub):
#     if (lb<ub):
#         loc = partition(arr,lb,ub)
#         quickSort(arr,lb,loc-1)
#         quickSort(arr,loc+1,ub)


# arr = [9,8,7,6,5,4,3,2,1]
# n= len(arr)-1
# quickSort(arr,0,len(arr))
# print(arr)
