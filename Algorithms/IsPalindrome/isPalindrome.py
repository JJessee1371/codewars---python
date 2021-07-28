def isPalindrome(str):
    str = str.lower()
    if str == str[::-1]:
        print("This word is a palindrome!")
    else:
        print("Sorry, this word is not a palindrome.")

exString = "Able was I ere I saw Elba"
isPalindrome(exString)