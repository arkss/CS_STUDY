arr = [6, 5, 1, 4, 7, 2, 3]

# 1번 방법
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


# 2번 방법 ===============================================
def partition(arr, start, end):
    pivot = arr[start] # pivot 은 임의의 값이기 때문에 첫번째 원소로 잡아도 상관 없음
    left = start + 1
    right = end
    done = False

    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and pivot <= arr[right]:
            right -= 1
        
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    arr[start], arr[right] = arr[right], arr[start]
    return right

def quick_sort2(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quick_sort2(arr, start, pivot - 1)
        quick_sort2(arr, pivot + 1, end)
    return arr

# 2번 방법 끝 ===============================================