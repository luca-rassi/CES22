def is_palindrome(str):
    # Returns True if a word, phrase or number is a palindrome
    str = str.replace(" ", "")
    n = int(len(str)/2) + 1

    for i in range(n):
        if str[i] != str[-i - 1]:
            return False
    return True
