def to_nato(words):
    return ' '.join(NATO.get(char, char) for char in words.upper() if char != ' ')
