def checkout():
    prices = []
    
    while True:
        price = float(input("Enter price (0 to stop): "))
        
        if price == 0:
            break
        
        prices.append(price)
    
    if len(prices) > 0:
        total = 0
        for p in prices:
            total = total + p
        
        print("Total:", total)
        print("Average:", total / len(prices))
        print("Items:", len(prices))

checkout()
