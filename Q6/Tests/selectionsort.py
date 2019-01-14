def selection_sort(a):
    n = len(a)
    for i in range(0, n):
        elem = a[i]
        pos = i
        for j in range(i+1, n):
            if a[j] < elem:
                elem = a[j]
                pos = j
        temp = a[i]
        a[i] = a[pos]
        a[pos] = temp
    return a


print(selection_sort([6,5,4,3,7,8,6,4,1,6,9,8,4,1,6,7]))


