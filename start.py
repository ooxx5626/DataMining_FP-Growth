import node_class
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
simpDat = loadSimpDat()
print(simpDat)
initSet = node_class.createInitSet(simpDat)
for t in initSet:
    print(t)
myFPtree, myHeaderTab = node_class.createTree(initSet, 1)
myFPtree.disp()
print(node_class.findPrefixPath(myHeaderTab['Beer'][1]))