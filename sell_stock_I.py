prices = [7,1,5,3,6,4]



def stock(prices):
    max_price = 0 
    min_price = float("inf")
    for price in range(len(prices)):
        if prices[price] < min_price:
            min_price = prices[price]
        
        profit = prices[price] - min_price
    
        if profit > max_price:
            max_price = profit
    
    return max_price

print(stock(prices))




    