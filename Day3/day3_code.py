import re #regular expressions

file = open('Day3/input.txt', 'r')
lines = file.readlines()

pattern = r'([0-9]+)'
nonsymbolchars = ['0','1','2','3','4','5','6','7','8','9','.','\n']
gearchar = '*'

def checkCellForSymbol(match:re.Match, linestocheck:list[int], columnstocheck:list[int]):
    for linecheck in linestocheck:
        for columncheck in columnstocheck:
            character = lines[linecheck][columncheck]
            if character not in nonsymbolchars:
                #print(character, match.group(0))
                #print(match.group(0))
                return True
    return False

def getLinesToCheck(currentlineindex:int):
    linestocheck = []
    previouslineindex = currentlineindex - 1
    nextlineindex = currentlineindex + 1
    if not(previouslineindex < 0):
        linestocheck.append(previouslineindex)
    linestocheck.append(currentlineindex)
    if not(nextlineindex >= numberoflines):
        linestocheck.append(nextlineindex)
    return linestocheck

def getColumnsToCheck(match:re.Match):
    columnstart = match.start() - 1
    columnend = match.end() + 1
    columnstocheck = list(range(columnstart, columnend))
    try: 
        columnstocheck.remove(-1)
    except:
        pass
    try:
        columnstocheck.remove(lengthofline)
    except:
        pass
    return columnstocheck

sum = 0
iterator = 0
numberoflines = len(lines)
for line in lines:
    lengthofline = len(line)
    digitmatches = re.finditer(pattern, line) 
    digitmatcheslist = [x for x in digitmatches]
    #print(digitmatcheslist)

    linestocheck = getLinesToCheck(iterator)
    for match in digitmatcheslist:
        columnstocheck = getColumnsToCheck(match)
        if checkCellForSymbol(match, linestocheck, columnstocheck) == True:
            sum += int(match.group(0))

    iterator += 1

print("Part 1 final sum =", sum)