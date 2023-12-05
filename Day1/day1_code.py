import re #regular expressions

file = open('Day1/input.txt', 'r')
lines = file.readlines()

pattern = '[0-9]'

sum = 0
for line in lines:
    digitmatches = re.finditer(pattern, line) 
    digitmatcheslist = [x.start() for x in digitmatches]
    #print(digitmatcheslist)
    firstdigitindex = digitmatcheslist[0]
    lastdigitindex = digitmatcheslist[-1]
    #print(firstdigitindex, lastdigitindex)
    firstdigit = line[firstdigitindex]
    lastdigit = line[lastdigitindex]
    #print(firstdigit, lastdigit)
    number = int("".join((firstdigit, lastdigit)))
    #print(number)
    sum += number

print("Final sum =", sum)