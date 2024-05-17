import timeit


def find_min_coins(amount_test, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount_test + 1)
    dp[0] = 0
    coin_used = [[] for _ in range(amount_test + 1)]
    
    for i in range(1, amount_test + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin_used[i - coin] + [coin]
    
    result = {}
    for coin in coin_used[amount_test]:
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
    
    return result


amount = 113

used_coins = find_min_coins(amount)
print(f"Використані монети для суми {amount}: {used_coins}")

find_coins_time = timeit.timeit('find_min_coins(amount)', globals=globals(), number=10)
print(f"Час виконання find_min_coins для суми {amount}: {find_coins_time} секунд\n")

amount_test = 1000

used_coins = find_min_coins(amount_test)
print(f"Використані монети для суми {amount_test}: {used_coins}")

find_coins_time = timeit.timeit('find_min_coins(amount_test)', globals=globals(), number=10)
print(f"Час виконання find_min_coins для суми {amount_test}: {find_coins_time} секунд\n")

amount_test_2 = 10000

used_coins = find_min_coins(amount_test_2)
print(f"Використані монети для суми {amount_test_2}: {used_coins}")

find_coins_time = timeit.timeit('find_min_coins(amount_test_2)', globals=globals(), number=10)
print(f"Час виконання find_min_coins для суми {amount_test_2}: {find_coins_time} секунд")
