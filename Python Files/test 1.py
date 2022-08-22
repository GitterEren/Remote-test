a=[i for i in range(9)]
b=[e for e in range(2,11)]
par=zip(a,b)
for c,d in par:
    print(f'{c} is 2 less than {d}')

