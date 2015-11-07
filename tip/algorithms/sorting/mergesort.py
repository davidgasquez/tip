def merge(a, b):
    if len(a) * len(b) == 0:
        return a + b

    v = (a[0] < b[0] and a or b).pop(0)
    return [v] + merge(a, b)


def mergesort(list):
    if len(list) < 2:
        return list

    m = len(list) / 2
    return merge(mergesort(list[:m]), mergesort(list[m:]))
