def merge_sort(a):
    merge_sort_rec(a, 0, len(a) - 1)

def merge_sort_rec(a, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort_rec(a, low, mid)
        merge_sort_rec(a, mid + 1, high)
        merge(a, low, mid, high)

def merge(a, low, mid, high):
    left = a[low:(mid + 1)]
    right = a[(mid + 1):(high + 1)]

    i = 0
    j = 0

    for k in range(low, high + 1):
        if i < len(left) and (j >= len(right) or left[i] <= right[j]):
            a[k] = left[i]
            i += 1
        elif j < len(right) and (i >= len(left) or right[j] <= left[i]):
            a[k] = right[j]
            j += 1
