def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u']

    stringLength = len(string_)
    result = ''

    for i in range(stringLength):
        if string_[i].lower() in vowels:
            continue
        result += string_[i]
    return result
print(disemvowel('This website is for losers LOL!'))
