def min_coins(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    
    used_coins = [-1] * (target + 1)
    
    for coin in coins:
        for i in range(coin, target + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used_coins[i] = coin
    
    if dp[target] == float('inf'):
        return -1, []
    
    result_coins = []
    current = target
    while current > 0:
        result_coins.append(used_coins[current])
        current -= used_coins[current]
    
    return dp[target], result_coins

if __name__ == "__main__":
    coins_sets = [
        ([1, 2, 5], 11),
        ([2, 3, 7], 12),
        ([1, 3, 4], 6),
        ([5, 10, 25], 30)
    ]
    
    for coins, target in coins_sets:
        min_count, coin_list = min_coins(coins, target)
        print(f"Moedas disponíveis: {coins}")
        print(f"Valor alvo: {target}")
        print(f"Mínimo de moedas necessárias: {min_count}")
        print(f"Moedas utilizadas: {coin_list}")
        print("-" * 40)
