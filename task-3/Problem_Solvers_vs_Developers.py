line1 = input()
line2 = input()
line3 = input()

line1 = line1.split(" ")
line2 = line2.split(" ")
line3 = line3.split(" ")

n = int(line1[0])
m = int(line1[1])

pn = [int(num) for num in line2]
pm = [int(num) for num in line3]

if max(pn) > max(pm):
    print ("NO")
else:
    pn.sort()
    pm.sort()
    
    min_power = 0
    for i in range(len(pn)):
        for j in range(len(pm)):
            if pm [j] > pn [0]:
                min_power += pm[j]
                pm.pop(j)
                pn.pop(0)
                break
    if len(pn) == 0:
        print ("YES")
        print (min_power)
    else:
        print("NO")
