def positive_sum(arr):
    n = []
    for i in arr:
        if i > 0:
            n.append(i)
    sum = 0
    for i in n:
        sum += i
    return sum
