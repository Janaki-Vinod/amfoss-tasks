input()
n = [int(num) for num in input().split(" ")]

n.sort()

t = [1]
for i in range(1,len(n)):
    if n[i]==n[i-1]:
        t[-1] += 1
    else:
        t.append(1)

print (max(t),len(t))