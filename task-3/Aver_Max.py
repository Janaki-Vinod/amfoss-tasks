num_of_cases = int(input())

cases = []
for i in range (num_of_cases):    
    line1 = input()
    line2 = input()
    line1 = line1.split(" ")
    line2 = line2.split(" ")
    cases.append([line1,line2])

for case in cases:
    n = int(case[0][0])
    k = int(case[0][1])
    
    seq = [float(num) for num in case[1]]
    if k != 0:
        seq = [abs(num) for num in seq]
    
    avg = max(seq)
    print (avg)