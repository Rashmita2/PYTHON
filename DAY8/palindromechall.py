def checkpalindrome(word):
    return word[::-1].casefold() == word.casefold()

word = input('Please enter a word: ')
if checkpalindrome(word):
    print('it is palindrome')
else:
    print('not a plaindrome')

#check if the sentence if alphanumberic

