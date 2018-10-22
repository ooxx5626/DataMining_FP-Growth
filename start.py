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
def getPattern(myHeaderTab, patterns):
    
    for top in myHeaderTab:
        pats = node_class.findPrefixPath(myHeaderTab[top][1])
        pattern = {}
        nodeName = myHeaderTab[top][1].name
        for pat in pats:
            # print(myHeaderTab[top][1].name)
            
            
            # pattern[str(nodeName)]=pattern.get(str(nodeName), 0)+pats[pat]
            # patterns[pat]=patterns.get(pat, 0)+pats[pat]
            pattern[pat]=pattern.get(pat, 0)+pats[pat]
            # print(pattern)
            
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
            for subtop in subHeaderTab:
                subpats = node_class.findPrefixPath(subHeaderTab[subtop][1])
                for subpat in subpats:
                    print(subpat)
                    # patterns[subpat]=patterns.get(pat, 0)+subpats[subpat]
simpDat = loadSimpDat()
# simpDat = readAndParser.readAndParser("data.ntrans_100")
# print("simpDat", simpDat)
initSet = node_class.createInitSet(simpDat)
myFPtree, myHeaderTab = node_class.createTree(initSet, 2) 
save = []
myFPtree.disp(save = save)
for s in save:
    print(s)

patterns = {}
getPattern(myHeaderTab, patterns)
for top in myHeaderTab:
    HeaderNode = myHeaderTab[top]
    # print(myHeaderTab[top][1].name,myHeaderTab[top][0])
    patterns[frozenset([HeaderNode[1].name])] = HeaderNode[0]
print(str(patterns).replace('frozenset(','').replace(')',''))

# print(node_class.findPrefixPath(myHeaderTab['Milk'][1]))