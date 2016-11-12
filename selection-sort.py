def selection_sort(a):
    for j in range(len(a) - 1):
        m = j
        for i in range(j + 1, len(a)):
            if a[i] < a[m]:
                m = i
        temp = a[j]
        a[j] = a[m]
        a[m] = temp
