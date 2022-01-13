sig1 = [0, 0, 1]
num = 9

def tribonnaci(signature, n):
    if len(signature) == 0 or n == 0:
        print([])
    if n < 3:
        print(signature[0:n])

    result = signature
    x = n - 3
    start = 0
    end = 3
    while x > 0:
        toAdd = result[start:end]
        result.append(toAdd[0] + toAdd[1] + toAdd[2])
        start += 1
        end += 1
        x -= 1
    print(result)

tribonnaci(sig1, num)


# Best practices solution
def tribonacci2(signature, n):
    res = signature[:n]
    for i in range(n - 3):
        res.append(sum(res[-3:]))
    print(res)