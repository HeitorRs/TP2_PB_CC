import time

def fibonacci(n):
    if n <= 0:
        raise ValueError("A posição na sequência deve ser positiva.")
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_memo(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


n = 30

start = time.time()
fib_rec = fibonacci(n)
end = time.time()
print(f"Sem memorização: Fibonacci({n}) = {fib_rec} | Tempo: {end - start:.5f} segundos")

start = time.time()
fib_mem = fibonacci_memo(n)
end = time.time()
print(f"Com memorização: Fibonacci({n}) = {fib_mem} | Tempo: {end - start:.5f} segundos")