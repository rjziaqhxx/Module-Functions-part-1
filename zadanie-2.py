def func(a,b):
    if a > b:
        max = a
        min = b
    else:
        max = b
        min = a
    l=[]
    for i in range(min, max+1):
        if i % 2 == 0:
            l.append(i)
    print(l)

func(8,14)