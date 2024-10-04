def func(a,b):
    if a > b:
        max = a
        min = b
    else: 
        max = b
        min = a
    l = []
    for i in range(min,max+1):
        l.append(i)
    return l

print(func(30,13))