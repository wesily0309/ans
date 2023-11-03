a=[]
b=input()
for i in range(3):
    a.append(input())
nanb=[]
for i in range(len(a)):
    an=[a[i],'為']
    aa=0
    bb=0
    for u in range(len(a[i])):
        if a[i][u]==b[u]:
            aa+=1
        elif a[i][u] in b:
            bb+=1
    an.append(f'{aa}A{bb}B')
    nanb.append(an)
for i in nanb:
    print(' '.join(i))