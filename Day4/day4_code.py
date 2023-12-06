import re #regular expressions

pattern = r'([0-9]+)'

file = open('Day4/input.txt', 'r')
lines = file.readlines()

class Game:
    def __init__(self, gameid:int, winningnumbers:list[int], playernumbers:list[int]):
        self.gameid = gameid
        self.winningnumbers = winningnumbers
        self.playernumbers = playernumbers
    def winningPlayerNumbers(self):
        matchingnumbers = []
        for playernumber in self.playernumbers:
            if playernumber in self.winningnumbers:
                matchingnumbers.append(playernumber)
        return matchingnumbers
    def winningPlayerNumbersCount(self):
        return len(self.winningPlayerNumbers())
    
def parseInputLine(line):
    colonsplit = line.split(':')
    gameid = int(''.join(x for x in colonsplit[0] if x.isdigit()))
    pipesplit = colonsplit[1].split('|')

    winningnumbersstring = pipesplit[0]
    rewinningnumbers = re.finditer(pattern, winningnumbersstring) 
    winningnumberslist = [int(x.group(0)) for x in rewinningnumbers]
    playernumbersstring = pipesplit[1]
    replayernumbers = re.finditer(pattern, playernumbersstring) 
    playernumberslist = [int(x.group(0)) for x in replayernumbers]

    return Game(gameid, winningnumberslist, playernumberslist)

print("\n\n---Part 1---")
totalpointssum = 0
gamedict = {} #For part 2, gamedict = {gameid:int: {'game': Game, 'copies': int}}
for line in lines:
    gameline = parseInputLine(line)
    gamelinewinningnumbercount = gameline.winningPlayerNumbersCount()
    gamepoints = 0
    if gamelinewinningnumbercount > 0:
        gamepoints = 2**(gamelinewinningnumbercount - 1)
        totalpointssum += gamepoints
    print("Gameid=",gameline.gameid,"Points=",gamepoints)
    #part 2 init
    gamedict[gameline.gameid] = {'game': gameline, 'copies': 1}

print("Part 1: Sum of all game points =", totalpointssum)

#Part 2:

def updateNextGamesCopies(gameid, addcopies):
    nextgameid = gameid + 1
    matchingnumberscount = game.winningPlayerNumbersCount()
    for i in range(nextgameid, nextgameid + matchingnumberscount):
        gamedict[i]['copies'] += addcopies
    return True

print("\n\n---Part 2---")
totalcopies = 0
for book in gamedict.values():
    game = book['game']
    gameid = game.gameid
    copies = book['copies']
    updateNextGamesCopies(gameid, copies)
    print("GameID=",game.gameid, "Copies=", copies)
    totalcopies += copies
print("Part 2: Sum of total copies =" ,totalcopies)