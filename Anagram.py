def clean(word):
    #removes no alpha chars & sets word to lowercase
    result = ""
    for char in word.lower():
        if char.isalpha():
            result += char
    return result


def anagram1(w1, w2):
    w1 = clean(w1)
    w2 = clean(w2)
    if len(w1) != len(w2):
        return False
    else:
        for char in w1:
            if w1.count(char) != w2.count(char):
                return False
        return True

def anagram2(w1, w2):
    w1 = clean(w1)
    w2 = clean(w2)

    w1 = "".join(sorted(w1))
    w2 = "".join(sorted(w2))

    return w1 == w2

print(anagram2("dog", "god"))