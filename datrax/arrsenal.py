def sumup(arr):
    if not arr:
        raise ValueError("Array is empty")
    total = 0
    i=0
    n = len(arr)
    while i<n:
        total += arr[i]
        i += 1
    return total
        
def maxout(arr):
    if not arr:
        raise ValueError("Array is empty")
    max_val = arr[0]
    i = 1
    n = len(arr)
    while i<n:
        v = arr[i]
        if v > max_val:
            max_val = v
        i+=1
    return max_val
    
def minout(arr):
    if not arr:
        raise ValueError("Array is empty")
    min_val = arr[0]
    i = 1
    n = len(arr)
    while i<n:
        v = arr[i]
        if v < min_val:
            min_val = v
        i+=1
    return min_val
    
def fliparr(arr: list) -> list:
    left = 0
    right = len(arr)-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
    
def uniqarr(arr: list) -> list:
    result = []
    for val in arr:
        if val not in result:
            result.append(val)
    return result
    
def ascend(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    
def descend(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def locate(arr: list, element) -> list:
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1  

def freq(arr: list, element) -> list:
    count = 0
    for val in arr:
        if val == element:
            count += 1
    return count

def mergearr(arr1: list, arr2: list) -> list:
    result = []
    for val in arr1:
        result.append(val)
    for val in arr2:
        result.append(val)
    return result
    
def cutarr(arr: list, start: int, end: int, step: int = 1) -> list:
    result = []
    i = start
    while i < end and i < len(arr):
        result.append(arr[i])
        i += step
    return result
    
def rotarr(arr: list, k: int) -> list:
    n = len(arr)
    k %= n
    return arr[-k:] + arr[:-k]

def inject(arr: list, pos: int, value) -> list:
    result = []
    for i in range(len(arr)):
        if i == pos:
            result.append(value)
        result.append(arr[i])
    if pos >= len(arr):  
        result.append(value)
    return result

def zapval(arr: list, value) -> list:
    result = []
    for val in arr:
        if val != value:
            result.append(val)
    return result

def zapindex(arr: list, index: int) -> list:
    result = []
    for i in range(len(arr)):
        if i != index:
            result.append(arr[i])
    return result
    
