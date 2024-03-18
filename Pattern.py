def patternCreator(num):
    n = "10"
    result = ""

    for i in range(0, num):
        if i % 2 == 0:
            result += n[0]
        else:
            result += n[1]
        
        print(result)

print(patternCreator(4))