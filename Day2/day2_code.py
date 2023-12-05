gameList = []
gameidsum = 0
validgameconditions = {'red': 12, 'green': 13, 'blue': 14}
sumofcubepowers = 0

file = open('Day2/input.txt', 'r')
lines = file.readlines()

class Game:
    def __init__(self, gameid:int, countred:int, countgreen:int, countblue:int):
        self.gameid = gameid
        self.countred = countred
        self.countgreen = countgreen
        self.countblue = countblue
    def __str__(self):
        return "{gameid}: Red={red}, Green={green}, Blue={blue}".format(gameid=self.gameid, red=self.countred, green=self.countgreen, blue=self.countblue)
    def isValid(self, validgameconditions):
        return self.countred <= validgameconditions['red'] and self.countgreen <= validgameconditions['green'] and self.countblue <= validgameconditions['blue']
    def cubepowers(self):
        return game.countred * game.countgreen * game.countblue

for line in lines:
    colonsplit = line.split(':')
    gameid = int(''.join(x for x in colonsplit[0] if x.isdigit()))
    semisplit = colonsplit[1].split(';')

    highred = 0
    highgreen = 0
    highblue = 0

    for batch in semisplit:
        commasplit = batch.split(',')
        for colour in commasplit:
            count = int(''.join(x for x in colour if x.isdigit()))
            if 'red' in colour and count > highred:
                highred = count
            if 'green' in colour and count > highgreen:
                highgreen = count
            if 'blue' in colour and count > highblue:
                highblue = count

    thisgame = Game(gameid, highred, highgreen, highblue)
    gameList.append(thisgame)

for game in gameList:
    if game.isValid(validgameconditions):
        gameidsum += game.gameid
    sumofcubepowers += game.cubepowers()
print("GameID sum of valid games = ", gameidsum)
print("Sum of cube powers = ", sumofcubepowers)