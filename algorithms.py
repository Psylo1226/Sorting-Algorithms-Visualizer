def bubble_sort(draw_info):
    arr = draw_info.arr

    for i  in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            num1 = arr[j]
            num2 = arr[j+1]

            if num1>num2:
                arr[j], arr[j+1]=arr[j+1], arr[j]
                draw_info.draw_list(True)
                yield True

def insertion_sort(draw_info):
    arr=draw_info.arr

    for i in range(1, len(arr)):
        current=arr[i]
        j = i - 1
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            arr[j + 1] = current
            draw_info.draw_list(True)
            yield True

def selection_sort(draw_info):
    arr=draw_info.arr

    for i in range(len(arr)):
        min_index=i

        for j in range(i+1, len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        (arr[i], arr[min_index])=(arr[min_index], arr[i])
        draw_info.draw_list(True)
        yield True

def partition(draw_info, low, high):
    arr=draw_info.arr

    pivot=arr[high]
    i=low-1

    for j in range(low, high):
        if arr[j]<=pivot:
            i+=1
            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    return i+1

def quick_sort(draw_info):
    arr=draw_info.arr

    def quick_sort_build(draw_info, low, high):
        if low < high:
            pi = partition(draw_info, low, high)
            quick_sort(draw_info)
            draw_info.draw_list(True)
            yield True
            yield from quick_sort_build(draw_info, low, pi - 1)
            yield from quick_sort_build(draw_info, pi + 1, high)

    yield from quick_sort_build(draw_info, 0, len(arr) - 1)

def heapify(draw_info, n, i):
    heapify = True
    arr=draw_info.arr

    while heapify:
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            (arr[i], arr[largest]) = (arr[largest], arr[i])
            i = largest
        else:
            heapify = False

def heap_sort(draw_info):
    arr=draw_info.arr
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(draw_info, n, i)
        draw_info.draw_list(True)
        yield True

    for i in range(n-1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(draw_info, i, 0)
        draw_info.draw_list(True)
        yield True

def merge(draw_info, l, m, r ):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = draw_info.arr[l + i]

    for j in range(0, n2):
        R[j] = draw_info.arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            draw_info.arr[k] = L[i]
            i += 1
        else:
            draw_info.arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        draw_info.arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        draw_info.arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(draw_info):
    arr=draw_info.arr

    def merge_sort_build(draw_info, l, r):
        if l < r:
            m = (l+(r-1))//2
            yield from merge_sort_build(draw_info, l, m)
            yield from merge_sort_build(draw_info, m+1, r)
            merge(draw_info, l, m, r)
            draw_info.draw_list(True)
            yield True

    yield from merge_sort_build(draw_info, 0, len(arr) - 1)

def counting_sort(draw_info, place):
    arr=draw_info.arr
    n=len(arr)

    output=[0] * n
    count=[0] * 10

    for i in range(0, n):
        index = arr[i] // place
        count[(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = n-1
    while i >= 0:
        index= arr[i] // place
        output[count[index % 10]-1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, n):
        arr[i] = output[i]

def radix_sort(draw_info):
    arr=draw_info.arr
    max_element = max(arr)

    place = 1
    while max_element // place > 0:
        counting_sort(draw_info, place)
        place += 1
        draw_info.draw_list(True)
        yield True

def shell_sort(draw_info):
    arr=draw_info.arr
    n=len(arr)
    gap=n//2

    while gap>0:
        for i in range(gap, n):
            temp=arr[i]
            j=i
            while j>=gap and arr[j - gap]>temp:
                arr[j]=arr[j - gap]
                j-=gap
                i-=gap
            arr[j]=temp
            draw_info.draw_list(True)
            yield True
        gap//=2

def cocktail_sort(draw_info):
    arr=draw_info.arr
    swap = True
    start = 0
    end = len(arr) - 1

    while swap:
        swap = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True
        if not swap:
            end = end-1
        for i in range(end-1, start-1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True
        start = start+1
        draw_info.draw_list(True)
        yield True

def counting_sort2(draw_info):
    arr=draw_info.arr
    n=len(arr)
    max_val = max(arr)

    m = max_val + 1
    count = [0] * m

    for a in arr:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1
            draw_info.draw_list(True)
            yield True
