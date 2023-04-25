def square_digits(num):
    s = str(num)
    n = []
    for i in s:
        p = str(int(i) ** 2)
        n.append(p)
    t = "".join(n)
    return int(t)
