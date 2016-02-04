# Within a file, search for occurances of numbers (multiple), return those and add the total
import re
totalValue = 0
totalValueCount = 0
hand = open('ex2B.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('([0-9]+)', line)
    if len(x) >= 1 :
        for element in x :
            totalValueCount = totalValueCount + 1
            totalValue = totalValue + int(element)
print ("==========================================")
print ("Count of found numbers ")
print totalValueCount
print ("Sum of found numbers " )
print totalValue
print ("==========================================")
