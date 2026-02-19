def tiers(customers):
    bronze = 0
    silver = 0
    gold = 0
    
    for name in customers:
        amount = customers[name]
        
        if amount < 1000:
            bronze = bronze + 1
        elif amount < 5000:
            silver = silver + 1
        else:
            gold = gold + 1
    
    print("Bronze:", bronze)
    print("Silver:", silver)
    print("Gold:", gold)

tiers({
    "Luke": 800,
    "Leia": 2500,
    "Han": 6000,
    "The Hairy One": 1200})
