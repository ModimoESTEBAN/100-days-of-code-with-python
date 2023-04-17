def desc(num):
    n = str(num)
    sn = list(n)
    return "".join(sorted(sn, reverse=True))

print(desc(123456789))
