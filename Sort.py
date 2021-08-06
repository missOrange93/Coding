#冒泡排序
def bubbleSort(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

#选择排序
def selectionSort(arr):
    for i in range(len(arr)-1):
        #记录最小数的索引
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

#插入排序
def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i - 1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex+1] = current
    return arr

#希尔排序(分组插入）
def shellSort(arr):
    import math
    gap = 1
    while (gap < len(arr)/3):
        gap = gap * 3 + 1
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > temp:
                arr[j+gap] = arr[j]
                j -= gap
            arr[j+gap] = temp
        gap = math.floor(gap/3)
    return arr

#归并排序  时间复杂度O(NlogN)：递归的部分为log2N；merge部分每次都要对N个数分成多组进行归并=>因此空间复杂度也为O(N)
def mergeSort(arr):
    import math
    if len(arr) < 2:
        return arr
    middle = math.floor(len(arr)/2)
    left, right = arr[0: middle], arr[middle: ]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

#快速排序  时间复杂度平均情况O(NlogN)，空间复杂度跟递归次数有关（递归造成的栈空间的使用），最好的情况O(logN),最差的情况O(N)
def quickSort(arr, left = None, right = None):
    if not left:
        left = 0
    if not right:
        right = len(arr) - 1
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr

def partition(arr, left, right):
    pivot = left
    index = pivot + 1 #index在未找到大数之前，和i同步向右移动，直到找到弟一个大数时开始标注。此后始终标注目前为止已经比较完成放好位置的最左边大数的index，以便于后面找到小数的时候进行交换
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)  #当i标注的是大数，大数本来就该在右侧所以不执行if；当i标注的是小数，将小数与index标注的弟一个大数进行交换，则可以确保所有小数在所有大数左边
            index += 1  #每次大小数交换后，index要右移一位标注当前第一个大数的index
        i += 1  #i始终标注下一个要进行比较的数字的index
    swap(arr,pivot,index-1)  #待所有大小数放好位置之后，将pivot与最后一个小数进行换位，则完成了一次分区操作
    return index-1  #返回分区后pivot的index

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

#快速排序更精简的模板
def QuickSort(arr, left = None, right = None):
    left = 0 if not isinstance(left,(int,float)) else left
    right = len(arr) - 1 if not isinstance(right,(int,float)) else right
    if left >= right:
        return
    #以left作为pivot来进行哨兵划分
    i, j = left, right
    while i < j:
        while arr[j] >= arr[left] and i < j:
            j -= 1
        while arr[i] <= arr[left] and i < j:
            i += 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[left] = arr[left], arr[i]  #把最后一个小数与pivot进行交换即完成一次划分
    #递归左右数组分别执行哨兵划分
    QuickSort(arr, left, i - 1)
    QuickSort(arr, i + 1, right)

#堆排序    时间复杂度为O(NlogN)：其中heapify部分每次二分左右子树只需调整一个子树，因而复杂度为为log2N；而heapSort部分for循环进行n次；空间上只对arr内部进行调整/删掉尾部索引，因此为O(1)
def buildMaxHeap(arr):
    for i in range(len(arr)//2 - 1, -1, -1):  #i从最后一个非叶子节点开始逆序取，最终首次建立最大的大顶堆
        heapify(arr,i)

def heapify(arr,i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    #通过比较当前的根节点和其左子树根/右子树根，选择其中最大的作为largest
    if left <= arrLen and arr[left] > arr[largest]:
        largest = left
    if right <= arrLen and arr[right] > arr[largest]:
        largest = right
    if largest != i:  #此时发生了节点数据交换，因此需重新调整largest节点（换入了原来i位置处较小的数）作为根节点的左子树/右子树使其成为大顶堆
        swap(arr,largest,i)
        heapify(arr,largest)

def swap(arr,i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    global arrLen
    arrLen = len(arr)-1  #角标的最大值
    buildMaxHeap(arr)  #首次必须全局建立大顶堆，而后续只需要调整发生数据变化的子树为大顶堆即可
    for i in range(len(arr)-1, 0, -1):
        swap(arr, i, 0)
        arrLen -=1  #arrLen作为全局变量，不断递减排除掉已经排好顺序的大数
        heapify(arr,0)
    return arr




