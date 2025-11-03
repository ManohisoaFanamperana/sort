def insertion_sort(arr):
    steps = []
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
            steps.append(a.copy())
        a[j + 1] = key
        steps.append(a.copy())
    return steps
