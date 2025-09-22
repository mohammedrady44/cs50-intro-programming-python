amount_due = 50
coins = [25,10,5]
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    user_coin = int(input("Insert Coin: "))
    if user_coin in coins:
        amount_due -= user_coin
print(f"Change Owed: {abs(amount_due)}")     
