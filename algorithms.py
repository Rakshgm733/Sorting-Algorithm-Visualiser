import time

def bubble_sort(array, draw_callback, speed, metrics):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                metrics["swaps"] += 1
            metrics["comparisons"] += 1
            draw_callback(array, [j, j + 1])
            time.sleep(speed)
    draw_callback(array)

def merge_sort(array, draw_callback, speed, metrics):
    def merge_sort_recursive(arr, l, r):
        if l < r:
            m = (l + r) // 2
            merge_sort_recursive(arr, l, m)
            merge_sort_recursive(arr, m + 1, r)
            merge(arr, l, m, r)

    def merge(arr, l, m, r):
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        i = j = 0
        k = l
        while i < len(left) and j < len(right):
            metrics["comparisons"] += 1
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            metrics["swaps"] += 1
            draw_callback(array, [k])
            k += 1
            time.sleep(speed)

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            metrics["swaps"] += 1
            draw_callback(array, [k])
            time.sleep(speed)

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            metrics["swaps"] += 1
            draw_callback(array, [k])
            time.sleep(speed)

    merge_sort_recursive(array, 0, len(array) - 1)
    draw_callback(array)

def quick_sort(array, draw_callback, speed, metrics):
    def partition(low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            metrics["comparisons"] += 1
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                metrics["swaps"] += 1
                draw_callback(array, [i, j])
                time.sleep(speed)
        array[i + 1], array[high] = array[high], array[i + 1]
        metrics["swaps"] += 1
        draw_callback(array, [i + 1, high])
        time.sleep(speed)
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    quick_sort_recursive(0, len(array) - 1)
    draw_callback(array)
