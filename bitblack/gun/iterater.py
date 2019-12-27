def fib(n):
    print("a")
    
    a = b = 1
    for i in range(1, n+1):
        if i == 1 or i == 2:
            yield 1
        else:
            a, b = a+b, a
            yield a

a = fib(10)
print(a)
print(list(a))
for i in a:
    print(i)

print([i for i in range(10)])

