def func(first,last):
    if first > last:
        max = first
        min = last
    else:
        max = last
        min = first
    l=[]
    for i in range(min, max+1):
        if i % 2 == 0:
            l.append(i)
    print(l)

func(8,14)