def longest_repetition(chars):
    max_char, max_count = '', 0
    char, count = '', 0
    for c in chars:
        if c != char:
            count, char = 0, c
        count += 1
        if count > max_count:
            max_char, max_count = char, count
    return max_char, max_count
