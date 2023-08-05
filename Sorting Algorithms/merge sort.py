def merge_sort(arr):
    if len(arr)>1:
        left_arr = arr[0:len(arr)//2]
        right_arr = arr[len(arr)//2:len(arr)]

        merge_sort(left_arr)
        merge_sort(right_arr)
        i=0 # for left array
        j=0 # for right array
        k=0 # merged arrray indecx

        while((i<len(left_arr)) and j<len(right_arr)):
            if (left_arr[i] < right_arr[j]):
                arr[k] = left_arr[i]
                i+=1
                k+=1
            else:
                arr[k] = right_arr[j]
                j+=1
                k+=1
        while(i<len(left_arr)):
            arr[k] = left_arr[i]
            k+=1
            i+=1
        while(j<len(right_arr)):
            arr[k] = right_arr[i]
            k+=1
            i+=1
        
        return arr

arr = [9,8,7,6,5,4,3,2,1]
t = merge_sort(arr)
print(t)




