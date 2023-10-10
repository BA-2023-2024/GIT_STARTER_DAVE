def GGT(a,b):
    while a!=b:
        if a>b:
            a= a-b
        else:
            b=b-a
    return a 

print(GGT(248,39))
