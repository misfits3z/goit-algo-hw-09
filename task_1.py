import random
import timeit

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    res = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            res[coin] = count
    return res

# amount_test = random.randint(10, 100)
amount = 113

used_coins = find_coins_greedy(amount)
print(f"Використані монети для суми {amount}: {used_coins}")

find_coins_time = timeit.timeit('find_coins_greedy(amount)', globals=globals(), number=10)
print(f"Час виконання find_coins_greedy{amount}: {find_coins_time} секунд\n")

amount_test = 1000

used_coins = find_coins_greedy(amount_test)
print(f"Використані монети для суми {amount_test}: {used_coins}")

find_coins_time = timeit.timeit('find_coins_greedy(amount_test)', globals=globals(), number=10)
print(f"Час виконання find_coins_greedy для суми {amount_test}: {find_coins_time} секунд\n")

amount_test_2 = 10000

used_coins = find_coins_greedy(amount_test_2)
print(f"Використані монети для суми {amount_test_2}: {used_coins}")

find_coins_time = timeit.timeit('find_coins_greedy(amount_test_2)', globals=globals(), number=10)
print(f"Час виконання find_coins_greedy для суми {amount_test_2}: {find_coins_time} секунд")