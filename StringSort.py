def alphaOrder(word):
    temp = ""
    w = list(word)
    a = True
    while a:
        a = False
        for i in range(0, len(w)-1):
            if ord(w[i]) > ord(w[i+1]):
                temp = w[i]
                w[i] = w[i+1]
                w[i+1] = temp
                a = True

    result = ''.join(w)
    return result

def revAlphaOrder(word):
    s = alphaOrder(word)
    result = s [::-1]
    return result

def freqOrder(word):
    for i in range

    return result
        
print(revAlphaOrder("goodbye"))
