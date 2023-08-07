def translate(phrase):
    vowels = "aeiouy"
    result = ""
    i = 0
    while i < len(phrase):
        if phrase[i] in vowels:
            result += phrase[i]
            i += 3
        elif phrase[i] == " ":
            result += phrase[i]
            i += 1
        else:
            result += phrase[i]
            i += 2
    return result

print (translate("hieeelalaooo"))