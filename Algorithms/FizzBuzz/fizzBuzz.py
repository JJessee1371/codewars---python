def fizzBuzz(arr):
    for i in arr:
        if i % 15 == 0:
            print("Fizz Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

exArray = [13, 14, 15, 16, 17, 18, 19, 20]
fizzBuzz(exArray)
