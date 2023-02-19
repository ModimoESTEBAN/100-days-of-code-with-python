def generate_hashtag(s):
    if len(s) > 140 or s == "":
        return False
    new_string = s.split()
    string = "#"

    for i in new_string:
        string += i.capitalize()

    return string
