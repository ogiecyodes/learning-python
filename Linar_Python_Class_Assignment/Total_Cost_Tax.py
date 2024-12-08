def total_cost(prices, tax_rate):
  tp = sum(prices)
  tax = (tax_rate * tp) / 100
  totalCost = sum((tp, tax))
  return totalCost
value = total_cost(prices=([10,20,30]), tax_rate=float(input("Enter tax rate applicable ")))
print(value)