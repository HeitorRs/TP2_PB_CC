def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print(f"Valor máximo da mochila: {knapsack(values, weights, capacity)}")

values2 = [10, 40, 50, 70]
weights2 = [1, 3, 4, 5]
capacity2 = 7

print(f"Valor máximo da mochila (conjunto 2): {knapsack(values2, weights2, capacity2)}")
