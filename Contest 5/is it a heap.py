def HeapType(arr):
    minHeap = True
    maxHeap = True
    n = len(arr)

    for i in range(n//2):
        left = (2*i)+1
        right = (2*i)+2

        if left < n:
            if arr[i] < arr[left]:
                maxHeap = False
            if arr[i] > arr[left]:
                minHeap = False

        if right < n:
            if arr[i] < arr[right]:
                maxHeap = False
            if arr[i] > arr[right]:
                minHeap = False

    if minHeap == False and maxHeap == False:
        result = "Neither"
    elif minHeap == True:
        result = "Min"
    else:
        result = "Max"
    
    return result


#input
n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = HeapType(arr)

print(result)