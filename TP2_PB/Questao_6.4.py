def pintar_cadeiras_dp(n, k):
    if n == 1:
        return k
    if k == 1:
        return 1 if n == 1 else 0
    
    dp = [0] * (n + 1)
    dp[1] = k
    dp[2] = k * (k - 1)
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] * (k - 1)
    
    return dp[n]

n = 5
k = 3
resultado = pintar_cadeiras_dp(n, k)
print(f"Há {resultado} maneiras de pintar {n} cadeiras com {k} cores.")

