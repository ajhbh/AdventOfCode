import re #regular expressions

file = open('Day1/input.txt', 'r')
lines = file.readlines()

pattern = r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))' #use lookahead and then select group one match to dealt with case of overlapping "oneight" where re.findall does not handle overlapping matches.
wordmap = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def getDigit(word):
    if len(word) == 1:
        return word
    else:
        return wordmap[word]


sum = 0
for line in lines:
    digitmatches = re.finditer(pattern, line) 
    digitmatcheslist = [x.group(1) for x in digitmatches]
    #print(digitmatcheslist)
    firstdigit = getDigit(digitmatcheslist[0])
    lastdigit = getDigit(digitmatcheslist[-1])
    #print(firstdigit, lastdigit)
    number = int("".join((firstdigit, lastdigit)))
    #print(number)
    sum += number

print("Final sum =", sum)