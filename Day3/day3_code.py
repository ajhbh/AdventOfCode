import re #regular expressions

file = open('Day3/input.txt', 'r')
lines = file.readlines()

pattern = r'([0-9]+)'
nonsymbolchars = ['0','1','2','3','4','5','6','7','8','9','.', '\n']

def checkNumberForSymbol(match):
    columnstart = match.start() - 1
    columnend = match.end()
    columnstocheck = list(range(columnstart, columnend+1))
    try: 
        columnstocheck.remove(-1)
    except:
        pass
    try:
        columnstocheck.remove(lengthofline)
        pass
    except:
        pass

    for linecheck in linestocheck:
        for columncheck in columnstocheck:
            character = lines[linecheck][columncheck]
            if character not in nonsymbolchars:
                print(character, match.group(0))
                #print(match.group(0))
                return True
    return False


sum = 0
iterator = 0
numberoflines = len(lines)
for line in lines:
    lengthofline = len(line)
    digitmatches = re.finditer(pattern, line) 
    digitmatcheslist = [x for x in digitmatches]
    #print(digitmatcheslist)

    linestocheck = []
    previouslineindex = iterator - 1
    nextlineindex = iterator + 1
    if not(previouslineindex < 0):
        linestocheck.append(previouslineindex)
    linestocheck.append(iterator)
    if not(nextlineindex >= numberoflines):
        linestocheck.append(nextlineindex)

    for match in digitmatcheslist:
        if checkNumberForSymbol(match) == True:
            sum += int(match.group(0))




    iterator += 1


print("Final sum =", sum)