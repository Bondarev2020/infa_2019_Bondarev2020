def change_possibilities_bottom_up(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            print(coin)
            print('higher_amount=', higher_amount)
            higher_amount_remainder = higher_amount - coin
            print('higher_amount_remainder=', higher_amount_remainder)
            print('ways_of_doing_n_cents[higher_amount]=', ways_of_doing_n_cents[higher_amount])
            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]
            print(ways_of_doing_n_cents)
    print (ways_of_doing_n_cents[amount])
change_possibilities_bottom_up(10, [5,2,3])

