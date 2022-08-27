# Métodos iterativo y recursivo para calcular la secuencia Fibonacci hasta el número Fibonacci F_n, para n >= 2.
# F_0 = 0, F_1 = 1, F_2 = 1, ...

def fib_iter(n):
    a = 0
    b = 1
    print(a, end=" ")
    print(b, end=" ")
    i = 2
    while i <= n:
        c = a + b
        print(c, end=" ")
        a = b
        b = c
        i = i + 1


def fib_recur(n):
    print(0, end=" ")
    print(1, end=" ")
    _fib_recur(n - 2, 0, 1)


def _fib_recur(n, a, b):
    if n < 0:
        return
    c = a + b
    print(c, end=" ")
    _fib_recur(n - 1, b, c)


print("Iterativo:")
fib_iter(15)
print()

print("Recursivo:")
fib_recur(15)
print()
