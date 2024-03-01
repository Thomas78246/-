price = [int(i) for i in input().split()]
n = len(price)
min_price = 10000
profit = []
for i in range(n):
    profit.append(max(0, price[i] - min_price))
    min_price = min(price[i], min_price)
print(max(profit))
