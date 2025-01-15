def fatorial(n):
    if n < 0:
        raise ValueError("O fatorial não é definido para números negativos.")
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

print(fatorial(0))
print(fatorial(1))
print(fatorial(5))
print(fatorial(10))

print(fatorial(15))

try:
    print(fatorial(-3))
except ValueError as e:
    print(e)
