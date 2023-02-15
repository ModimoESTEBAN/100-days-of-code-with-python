def solution(number):
    l = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            l.append(i)

    return sum(l)  
