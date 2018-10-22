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
def newSimpDat(arr):
    newDat = []
    for a in arr:
        for i in range(0,arr[a]):
            newDat.append(a)
    return newDat
    
simpDat = loadSimpDat()
# simpDat = readAndParser.readAndParser("data.ntrans_100")
# print("simpDat", simpDat)
initSet = node_class.createInitSet(simpDat)
myFPtree, myHeaderTab = node_class.createTree(initSet, 2) 
save = []
myFPtree.disp(save = save)
for s in save:
    print(s)

# print(myHeaderTab['Bread'][1].children)
patterns = {}
for top in myHeaderTab:
    pats = node_class.findPrefixPath(myHeaderTab[top][1])
    pattern = {}
    for pat in pats:
        # print(myHeaderTab[top][1].name)
        nodeName = myHeaderTab[top][1].name
        # print(pat)
        pattern[frozenset(nodeName)]=pattern.get(frozenset(nodeName), 0)+pats[pat]
        patterns[pat]=patterns.get(pat, 0)+pats[pat]
        pattern[pat]=pattern.get(pat, 0)+pats[pat]
        
    subDat = newSimpDat(pattern)
    subSet = node_class.createInitSet(subDat)
    subFPtree, subHeaderTab = node_class.createTree(subSet, 2) 
    # print(subHeaderTab)
    save=[]
    if subFPtree:
        subFPtree.disp(save=save)
        print('\n')
        for s in save:
            print(s)
    # topName = myHeaderTab[top][1].name
    # patterns[topName]=patterns.get(topName, 0) + myHeaderTab[top][0]
# str(trans).strip('frozenset()')
print(str(patterns).replace('frozenset(','').replace(')',''))

# print(node_class.findPrefixPath(myHeaderTab['Milk'][1]))