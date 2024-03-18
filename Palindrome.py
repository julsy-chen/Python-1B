def isPalindrome(word):
    # word is a string
    flipped = word [::-1]
    if flipped == word:
        return True
    else:
        return False
    
print(isPalindrome("dog"))

test = "tacocat"
print(isPalindrome(test))