def portfolio_value(portfolio):
    total = 0
    
    for stock in portfolio:
        shares = portfolio[stock]["shares"]
        price = portfolio[stock]["price"]
        
        value = shares * price
        print(stock, ":", value)
        
        total = total + value
    
    print("Total:", total)

portfolio_value({
    "AAPL": {"shares": 10, "price": 170},
    "TSLA": {"shares": 4, "price": 250},
    "AMZN": {"shares": 2, "price": 130}
})
