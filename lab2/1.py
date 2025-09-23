def is_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False


res = input("Enter a string: ")
print(is_palindrome(res))

