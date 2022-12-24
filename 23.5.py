a = int(raw_input('Give amount: '))

def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

a = fib()
a.next()
0
for i in range(a):
    print a.next(),