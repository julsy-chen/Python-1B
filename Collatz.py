def collatzSeq(num):
    c = 1
    
    while True:
        if num == 1:
            return c
        
        elif num % 2 == 0:
            num /= 2
            c += 1

        else:
            num = 3*num + 1
            c += 1

answer = 0
seqAnswer = 1
i = 1
while i in range(1, 1000000):
    if collatzSeq(i) > seqAnswer:
        answer = i
        seqAnswer = collatzSeq(i)

print(f"{answer} is the longest with a sequence of {seqAnswer}")