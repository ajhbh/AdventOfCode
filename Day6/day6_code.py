import re #regular expressions
import math

pattern = r'([0-9]+)'

file = open('Day6/input_part2.txt', 'r')
lines = file.readlines()

class Race:
    def __init__(self, totaltime:int, distance:int):
        self.totaltime = totaltime
        self.distance = distance
    def winningbuttontime(self):
        mintime = 0.5*(self.totaltime - math.sqrt(self.totaltime**2-4*self.distance) )
        maxtime = 0.5*(self.totaltime + math.sqrt(self.totaltime**2-4*self.distance) )
        if mintime == math.ceil(mintime):
            mintime+=1
        if maxtime == math.floor(maxtime):
            maxtime-=1
        winningtimes = range(math.ceil(mintime), math.floor(maxtime)+1)
        return winningtimes
    def winningbuttontimeways(self):
        return len(self.winningbuttontime())

    
def parseInputLine(line):
    renumbers = re.finditer(pattern, line) 
    numberslist = [int(x.group(0)) for x in renumbers]
    return numberslist

print("\n\n---Part 1---")
totalpointssum = 0
racedict = {} #For part 2, gamedict = {gameid:int: {'game': Game, 'copies': int}}

timelist = parseInputLine(lines[0])
distancelist = parseInputLine(lines[1])

i=0
for time in timelist:
    i+=1
    racedict[i] = Race(int(time), int(distancelist[i-1]))

print(timelist)
print(distancelist)

multiply = 1
for race in racedict.values():
    raceways = race.winningbuttontime()
    print("raceways:",raceways)
    racewayscount = race.winningbuttontimeways()
    print("racewayscount:",racewayscount)
    multiply = multiply*racewayscount
print("Part 1: NumberOfWaysMultiple=",multiply)

