def consCheck(word):
    vowels = "aeiou"
    c = 0

    for ch in word:
        if ch not in vowels:
            c += 1
    
    return c

def vowelCheck(word):
    vowels = "aeiou"
    c = 0

    for ch in word:
        if ch in vowels:
            c += 1

    return c

print(vowelCheck("hello"))