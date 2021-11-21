import math

n = int(input ())

variations = 0

sqn = math.ceil(math.sqrt(n))

for i in range(1,sqn):
    if not n%i:
        variations +=2

if sqn*sqn == n:
    variations += 1

print (variations)