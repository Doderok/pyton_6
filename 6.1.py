def nested_sum(t):
    s = 0
    for row in t:
        s += sum(row)
    return s

print(nested_sum(([1,2,3,4,5],[6,7,8,9,10])))