def vowelCount(str):
    count = 0
    for i in str:
        if i == "a" or i == "e" or i == "u" or i == "i" or i == "o":
            count += 1
    print(count)

exString = "Count the vowels in me!"
vowelCount(exString)
