def get_count(sentence):
    l = []
    s = sentence.replace(" ","")
    for i in s:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            l.append(i)
    return len(l)

