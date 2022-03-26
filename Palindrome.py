#Write a method is_palindrome(word) that takes in a string word and returns the true if the word is a palindrome, false otherwise.
def is_palindrome(s):
    if len(s) <=1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])

print(is_palindrome('madam'))
print(is_palindrome('radar'))
print(is_palindrome('book'))
print(is_palindrome(''))