def commissions(sales):
    for name in sales:
        commission = sales[name] * 0.10
        print(name, ":", commission)

commissions({
    "Alice": 5000,
    "Bob": 7000,
    "Carol": 3000
})
