line1 = input()
line2 = input()
line3 = input()

line1 = line1.split(" ")
line2 = line2.split(" ")
line3 = line3.split(" ")

X = int(line1[0])
N = int(line1[1])

cars=[[int(line2[i]),int(line3[i])] for i in range(X)]

time = []
for car in cars:
    if car[1] == 1:
        time.append(N+1-car[0])
    else:
        time.append(car[0])

print (max(time))