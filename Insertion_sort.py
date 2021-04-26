def insert_sort(arr):
    b = arr[:]
    for i in range(1,len(arr)):
        key = b[i]
        j = i-1
        while j>=0 and key<b[j]:
            b[j+1] = b[j]
            j=j-1
        b[j+1] = key
    return b

array = [5,2,1,6,4,3]
k = insert_sort(array)
print(array)
print(k)
