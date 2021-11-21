num_of_cases = int(input())

cases = []
for i in range (num_of_cases):    
    line1 = input()
    line2 = input()
    cases.append([line1,line2])

for case in cases:
    data = case[0].split(" ")
    spots = case[1].split(" ")
    spots = [[int(spot),int(spot)+1] for spot in spots]

    N = int(data[0])
    M = int(data[1])
    v = int(data[2])
    k = int(data[3])

    spots.sort()
    
    #Calculate spots separately
    for spot in spots:
        spot[0] -= k*v
        spot[1] += k*v

    #Remove rope overflow 
    for spot in spots:
        if spot[0] < 1:
            spot[0] = 1
        if spot[1] > N+1:
            spot[1] = N+1

    #Remove spot overlap
    for i in range(len(spots) - 1):
        if spots[i][1]>=spots[i + 1][0]:
            spots[i + 1][0] = spots[i][1]
            
    # print (spots)
    #Calculate unspotted length
    for spot in spots:
        N -= spot[1] - spot[0]
    
    print (N)