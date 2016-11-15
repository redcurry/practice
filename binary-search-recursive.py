def binary_search(a, v):
    return binary_search_rec(a, v, 0, len(a) - 1)

def binary_search_rec(a, v, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if v < a[mid]:
        return binary_search_rec(a, v, low, mid - 1)
    elif v > a[mid]:
        return binary_search_rec(a, v, mid + 1, high)
    else:
        return mid
