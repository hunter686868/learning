def fibonacci(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


#result = fibonacci(543340)

#print(result)

a = 10

b = a

a = 5

print(a, b)
