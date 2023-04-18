
def abbrev_name(name):
    n = name.split()
    first = n[0][0]
    second = n[1][0]
    return first + "." + second

print(abbrev_name("Steven Modimo"))

