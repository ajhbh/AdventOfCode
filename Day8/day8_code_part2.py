import re #regular expressions

pattern = r'([0-9A-Z]+)'

file = open('Day8/input_part1.txt', 'r')
lines = file.readlines()

class Node:
    def __init__(self, name, next_node_left=None, next_node_right=None):
        self.name = name
        self.next_node_left = next_node_left
        self.next_node_right = next_node_right
    def get_next_node_left(self):
        return self.next_node_left
    def get_next_node_right(self):
        return self.next_node_right
    def set_next_node_left(self, next_node_left):
        self.next_node_left = next_node_left
    def set_next_node_right(self, next_node_right):
        self.next_node_right = next_node_right
    def get_name(self):
        return self.name
    
def parseInputLine(line):
    renumbers = re.finditer(pattern, line) 
    numberslist = [x.group(0) for x in renumbers]
    return numberslist

print("\n\n---Part 1---")
mapdict = {}
line1 = lines.pop(0) #LR instructions
print("Instructions=",line1)
instructionslist = list(line1)
lines.pop(0) #remove empty line
for line in lines:
    mapline = parseInputLine(line)
    nodename = mapline[0]
    leftnodename = mapline[1]
    rightnodename = mapline[2]
    print("nodename=",nodename,"Left=",leftnodename,"Right=",rightnodename)
    leftnode = mapdict.get(leftnodename)
    if leftnode == None:
        leftnode = Node(leftnodename, None, None)
        mapdict[leftnodename] = leftnode
    rightnode = mapdict.get(rightnodename) #after left so in dictionary if L & R the same name
    if rightnode == None:
        rightnode = Node(rightnodename, None, None)
        mapdict[rightnodename] = rightnode
    node = mapdict.get(nodename)
    if node == None:
        node = Node(nodename, leftnode, rightnode)
        mapdict[nodename] = node
    else:
        node.set_next_node_left(leftnode)
        node.set_next_node_right(rightnode)


currentnodes = []

for node in mapdict.values():
    nodename = node.get_name()
    if nodename.endswith("A") == True:
        currentnodes.append(node)
print("startnodes count =",len(currentnodes))

numberofsteps = 0

def checkNodesListNamesEndWithZ():
    allEndWithZ = True
    for node in currentnodes:
        if node.name.endswith('Z') == False:
            return False
    if currentnodes == []:
        return False
    return allEndWithZ

while checkNodesListNamesEndWithZ() == False:
    if len(instructionslist) == 0 or instructionslist[0] == '\n':
        instructionslist = list(line1)
    currentinstruction = instructionslist.pop(0)
    numberofsteps += 1
    nextcurrentnodes = []
    for currentnode in currentnodes:
        if currentinstruction == 'L':
            currentnode = currentnode.get_next_node_left()
            nextcurrentnodes.append(currentnode)
        elif currentinstruction == 'R': 
            currentnode = currentnode.get_next_node_right()
            nextcurrentnodes.append(currentnode)
    currentnodes = nextcurrentnodes

print("Completed map. Number of steps taken =", numberofsteps)


# too long. Need to determine for each starting node loop how many steps until repeats and then find lowest common multiple?