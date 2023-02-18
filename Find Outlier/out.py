def find_outlier(integers):
    check_even = list(filter(lambda x : x % 2 == 0, integers))
    check_odd = list(filter(lambda x : x % 2 != 0, integers))

    if len(check_even) > len(check_odd):
        return int("".join(map(str, check_odd)))
    else:
        return int("".join(map(str, check_even)))

