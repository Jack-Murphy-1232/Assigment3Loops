def pitch_chart():
    
    revenues = []
    
    for year in range(1, 6):
        revenue = int(input("Enter revenue for Year " + str(year) + ": "))
        revenues.append(revenue)
    
    print("\nProjected Revenue Chart:\n")
    print("\nEach # represents $100\n")
    
    year = 1
    for revenue in revenues:
        bars = revenue // 100
        print("Year", year, ":", "#" * bars)
        year = year + 1


pitch_chart()
