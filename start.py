import node_class
import readAndParser
def loadSimpDat():
    Bread ="Bread"
    Beer = "Beer"
    Milk = "Milk"
    Egg = "Egg"
    Coffee = "Coffee"
    simpDat = [[Bread, Milk, Beer], 
    [Bread, Coffee], 
    [Bread, Egg], 
    [Bread, Milk, Coffee], 
    [Milk, Egg], 
    [Bread, Egg], 
    [Milk, Egg], 
    [Bread, Milk, Egg, Beer], 
    [Bread, Milk, Egg]
    ]
    return simpDat
def newSimpDat():
    Bread ="Bread"
    Beer = "Beer"
    Milk = "Milk"
    Egg = "Egg"
    Coffee = "Coffee"
    ban = "ban"
    newDat = [[Beer, ban]]
    return newDat
simpDat = loadSimpDat()
# simpDat = readAndParser.readAndParser("data.ntrans_100")
initSet = node_class.createInitSet(simpDat)
myFPtree, myHeaderTab = node_class.createTree(initSet, 2) 
# newSimpDat = newSimpDat()
# print("myHeaderTab : ", myHeaderTab)
# print(newSimpDat)
# node_class.updateHeaderTable(node_class.createInitSet(newSimpDat), 1, myHeaderTab)
# for d in newSimpDat:
#     node_class.updateTree(d, myFPtree, myHeaderTab, 1)
save = []
myFPtree.disp(save = save)
for s in save:
    print(s)
    
with open("save.txt", "w+") as f:
    for s in save:
        f.write(s)
        f.write('\n')
# print(myHeaderTab['Beer'])
# print(node_class.findPrefixPath(myHeaderTab['Beer'][1]))