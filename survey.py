def survey(data):
    counts = {}
    
    for item in data:
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1
    
    for item in counts:
        percent = counts[item] / len(data) * 100
        print(item, ":", round(percent), "%")

survey(["coffee", "tea", "coffee", "soda"])
