x = 2
y = 3.5
initcaps = 100

for i in range(21):
    y += 0.5

    if x < y:
        caps1 = x * initcaps
        caps2 = caps1 / y
        caps_total = initcaps + caps2
        profit = caps1 - caps_total
        percentage = profit / caps_total * initcaps
    else:
        caps1 = y * initcaps
        caps2 = caps1 / x
        caps_total = initcaps + caps2
        profit = caps1 - caps_total
        percentage = profit / caps_total * initcaps

    print("Iteration:", i)
    print("caps_total:", caps_total)
    print("profit:", profit)
    print("percentage:", percentage)
    print("---------------------------")
