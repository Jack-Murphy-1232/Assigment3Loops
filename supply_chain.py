def supply(warehouses):
    totals = {}
    
    for w in warehouses:
        inventory = w["inventory"]
        
        for item in inventory:
            if item in totals:
                totals[item] = totals[item] + inventory[item]
            else:
                totals[item] = inventory[item]
    
    print(totals)

supply([
    {"name": "A", "inventory": {"apples": 2000, "bananas": 1700}},
    {"name": "B", "inventory": {"apples": 3400, "bananas": 1200}}
])
