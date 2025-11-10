def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n- i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j+=1
    result += left[i:]+right[j:]
    return result

def quickSort(arr):
    if len(arr)<=1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x<pivot]
    mid = [x for x in arr if x==pivot]
    right = [x for x in arr if x>pivot]
    return quickSort(left)+mid+quickSort(right)
