money = int(input())
A = input().split(' ')
coins = [0] * len(A)
for i in range(len(A)):
    coins[i] = int(A[i])
def make_exchange(money, coins):
    for i in range(1, len(A[1]), 2):
        C.append(int(A[1][i]))
    ways_of_doing_n_cents = [0] * (money + 1)
    ways_of_doing_n_cents[0] = 1
    for coin in coins:
        for higher_amount in range(coin, money + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]
    print (ways_of_doing_n_cents[money])
make_exchange(money, coins)

