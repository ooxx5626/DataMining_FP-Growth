import node_class
import readAndParser
# import Queue
from collections import defaultdict
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

# def getPattern(myHeaderTab, patterns):
#     for top in  sorted(myHeaderTab, key=lambda p: p[1], reverse=False):
#         HeaderNode = myHeaderTab[top]
#         print(myHeaderTab[top][1].name,myHeaderTab[top][0])
#         print(myHeaderTab[top])
#         # path=[]
#         path =  defaultdict(dict)
#         findPath(myHeaderTab[top], myHeaderTab[top].name, path)

def findPath(myHeaderTab, item, path=[]):
    nodeName=myHeaderTab[1].name
    if nodeName==item:
        return path
    else:
        if myHeaderTab[1].children != {}:
            path.append(nodeName)
            for child in myHeaderTab[1].children:
                findPath(child, item, path)
        # else:
            
def getChildCount(myHeaderTab, count=0):
    for child in myHeaderTab.children:
        child = myHeaderTab.children[child]
        # print(child.children)
        if child.children == {}:
            count+=1
        else:
            count+=getChildCount(child)
    return count
def get_table(simpDat):
    table=[]
    for tr in simpDat:
        for i in tr:
            if i not in table:
                table.append(i)
    return table

# simpDat = loadSimpDat() 
                                             
simpDat = readAndParser.readAndParser("data.ntrans_1.ascii.tlen_5.nitems_1.npats_2")
table = get_table(simpDat) 
readAndParser.save_csv(table, simpDat, 'weka.csv')  
# print("simpDat", simpDat)
initSet = node_class.createInitSet(simpDat)
myFPtree, myHeaderTab = node_class.createTree(initSet, 2) 
save = []
myFPtree.disp(save = save)
for s in save:
    print(s)

patterns = {}
path_count=0
path=[]
for m in myHeaderTab:
    P_node = myHeaderTab[m][1]
    path_count+=getChildCount(P_node)
    # findPath(P_node,m, path)
        
# print(BFS(path_count))
    # patterns[frozenset([HeaderNode[1].name])] = HeaderNode[0]
# print(str(patterns).replace('frozenset(','').replace(')',''))

# print(node_class.findPrefixPath(myHeaderTab['Milk'][1]))