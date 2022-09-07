# Métodos iterativo y recursivo para calcular la secuencia Fibonacci hasta el número Fibonacci F_n, para n >= 2.
# F_0 = 0, F_1 = 1, F_2 = 1, ...

def fib_iter(n):
    seq = []
    a = 0
    b = 1
    seq.append(a)
    seq.append(b)
    i = 2
    while i <= n:
        c = a + b
        seq.append(c)
        a = b
        b = c
        i = i + 1
    return ' '.join([str(x) for x in seq])


def fib_recur(n):
    seq = [0, 1]
    _fib_recur(n - 2, 0, 1, seq)
    return ' '.join([str(x) for x in seq])


def _fib_recur(n, a, b, seq):
    if n < 0:
        return
    c = a + b
    seq.append(c)
    _fib_recur(n - 1, b, c, seq)

n = 15

print("Iterativo:")
print(fib_iter(n))

print()

print("Recursivo:")
print(fib_recur(n))
