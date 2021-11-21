n,m=map(int,input().split())
k=0
l=[]
while True:
    if n%2==0 and n>0:
        k=k+1
        n=n//2
    else:
        break
for i in range (1,m+1):
    p=i
    s=0
    while True:
        if i%2==0 and i>0:
            s=s+1
            i=i//2
        else:
            break
    if s<k:
        l.append(p)
print(len(l))
for j in l:
    print( j, end=" ")
