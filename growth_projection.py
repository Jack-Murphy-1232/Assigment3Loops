def growth_projection():
    initial_revenue = float(input("Enter initial revenue: "))
    growth_rate = float(input("Enter annual growth rate (%): "))
    
    revenue = initial_revenue
    
    print("\nRevenue Projection for 10 Years:")
    
    for year in range(1, 11):
        revenue = revenue * (1 + growth_rate / 100)
        print("Year", year, ":", revenue)

growth_projection()
