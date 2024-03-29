mode = 'Part2' #set mode = 'Part1' for first part of question or mode = 'Part2' for second part of question. Changes the seed parsing logic

file = open('Day5/input_batch.txt', 'r')
lines = file.readlines()

seeds = []
soilboundslist = []
fertilizerboundslist = []
waterboundslist = []
lightboundslist = []
tempboundslist = []
humidboundslist = []
locationboundslist = []

def mapping(numberToCheck:int, boundslist:list[tuple]):
    for bounds in boundslist:
        sourcerangebound = (int(bounds[1]), int(bounds[1]) + int(bounds[2]))
        if numberToCheck >= sourcerangebound[0] and numberToCheck < sourcerangebound[1]:
            #destinationrangebound = (bounds[0], bounds[0] + bounds[2])
            difference = int(bounds[0]) - int(bounds[1]) #numberToCheck + difference = result
            return numberToCheck + difference
        else:
            continue
    return numberToCheck
def reverseMapping(numberToCheck:int, boundslist:list[tuple]):
    for bounds in boundslist:
        sourcerangebound = (int(bounds[0]), int(bounds[0]) + int(bounds[2]))
        if numberToCheck >= sourcerangebound[0] and numberToCheck < sourcerangebound[1]:
            #destinationrangebound = (bounds[0], bounds[0] + bounds[2])
            difference = int(bounds[1]) - int(bounds[0]) #numberToCheck + difference = result
            return numberToCheck + difference
        else:
            continue
    return numberToCheck

def seedToLocation(seed):
    seedtosoil = mapping(seed, soilboundslist)
    soiltofertilizer = mapping(seedtosoil, fertilizerboundslist)
    fertilizertowater = mapping(soiltofertilizer, waterboundslist)
    watertolight = mapping(fertilizertowater, lightboundslist)
    lighttotemperature = mapping(watertolight, tempboundslist)
    temperaturetohumidity = mapping(lighttotemperature, humidboundslist)
    humiditytolocation = mapping(temperaturetohumidity, locationboundslist)
    return humiditytolocation

def parseSeedsLine(seedline, mode):
    seedsstring = seedline.split(':')[1]
    seedss = seedsstring.strip().split(' ')
    if mode == 'Part1':
        [seeds.append(int(x)) for x in seedss]
        return seeds
    elif mode == 'Part2':
        for i in range(int(len(seedss)/2)):
            expandseeds = range(int(seedss[2*i-1]))
            for j in expandseeds:
                seeds.append(int(seedss[2*i-2])+j)

def parseData(lines):
    seedline = lines[0]
    parseSeedsLine(seedline, mode)
    lines.pop(0)
    table = ''
    for line in lines:
        if line == 'seed-to-soil map:\n':
            table = 'soilboundslist'
        elif line == 'soil-to-fertilizer map:\n':
            table = 'fertilizerboundslist'
        elif line == 'fertilizer-to-water map:\n':
            table = 'waterboundslist'
        elif line == 'water-to-light map:\n':
            table = 'lightboundslist'
        elif line == 'light-to-temperature map:\n':
            table = 'tempboundslist'
        elif line == 'temperature-to-humidity map:\n':
            table = 'humidboundslist'
        elif line == 'humidity-to-location map:\n':
            table = 'locationboundslist'
        elif len(line)>4:
            thismap = line.strip().split(' ')
            thismap = [int(x) for x in thismap]
            thistuple = (thismap[0],thismap[1],thismap[2])
            writeToList(table, thistuple)

def writeToList(boundslistname:str, tupletowrite:tuple):
    if boundslistname == 'soilboundslist':
        soilboundslist.append(tupletowrite)
    elif boundslistname == 'fertilizerboundslist':
        fertilizerboundslist.append(tupletowrite)
    elif boundslistname == 'waterboundslist':
        waterboundslist.append(tupletowrite)
    elif boundslistname == 'lightboundslist':
        lightboundslist.append(tupletowrite)
    elif boundslistname == 'tempboundslist':
        tempboundslist.append(tupletowrite)
    elif boundslistname == 'humidboundslist':
        humidboundslist.append(tupletowrite)
    elif boundslistname == 'locationboundslist':
        locationboundslist.append(tupletowrite)

parseData(lines)
#print("InputSeeds=", seeds)
#results = {}
lowestseed = None
lowestlocation = None
for seed in seeds:
    location = seedToLocation(seed)
    #results[seed] = location
    if lowestlocation == None or lowestlocation > location:
        lowestlocation = location
        #lowestseed = seed
print("LowestSeed=", lowestseed, "LowestLocation=", lowestlocation)
