def cumsum(t):
    total = 0
    for x in t:
        total += x
        yield total
print(list(cumsum([25,46,31])))
