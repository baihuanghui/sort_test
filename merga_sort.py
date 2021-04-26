def merga(arr,l,m,r):
    '''

    :param arr: 待排数组
    :param l: 数组最左侧
    :param m: 数组中间分界
    :param r: 数组最右
    :return: 排完序的数组
    '''
    n1 = m-l+1
    n2 = r-m
    L = [0] * n1
    R = [0] * n2
    for i in range(0,n1):
        L[i] = arr[l+i]
    for j in range(0,n2):
        R[j] = arr[m+j+1]

    #归并临时数组到arr[l,r]

    i = 0  #初始化L的序列
    j = 0  #初始化R的序列
    k = l  #初始化归并子数组的索引

    while i<n1 and j<n2:
        if L[i]<R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k +=1
    #拷贝L剩余元素
    while i<n1:
        arr[k] = L[i]
        i+=1
        k+=1
    #拷贝R剩余元素
    while j<n2:
        arr[k] = R[j]
        j+=1
        k+=1

def mergaSort(arr,l,r):
    if l<r:
        m = int((l+(r-1))/2)
        mergaSort(arr,l,m)
        mergaSort(arr,m+1,r)
        merga(arr,l,m,r)

arr = [12,11,13,5,6,7]
n = len(arr)
print("给定的数组:")
print(arr)
mergaSort(arr,0,n-1)
print("\n排序后的数组")
print(arr)

