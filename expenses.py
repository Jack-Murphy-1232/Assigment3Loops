def expenses_report(expenses):
    grand_total = 0
    
    for category in expenses:
        total = 0
        
        for amount in expenses[category]:
            total = total + amount
        
        print(category, ":", total)
        grand_total = grand_total + total
    
    print("Grand Total:", grand_total)

expenses_report({
    "Travel": [500, 200],
    "Meals": [40, 60, 30],
    "Supplies": [100]
})
