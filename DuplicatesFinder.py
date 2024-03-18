def clean(w):
    result =""
    for ch in w:
        if ch.isalpha():
            result += ch
    return result

def duplicateFinder(w1, w2):
    w1 = clean(w1)
    w2 = clean(w2)

    result = []

    if len(w1) < len(w2):
        temp = w1 
        w1 = w2
        w2 = temp

    for ch in w2:
        if ch in w1 and ch not in result:
            result.append(ch)

    return result

print(duplicateFinder("food", "good"))
