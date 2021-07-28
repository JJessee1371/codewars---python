def maxNum(arr):
    result = arr[0]
    for i in arr:
        if i > result:
            result = i
    print(result)

exArray = [3, 1, 17, 5, 6, -3, 20, 0, -400]
maxNum(exArray)
