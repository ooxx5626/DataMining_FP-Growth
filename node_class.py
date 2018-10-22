class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode      #needs to be updated
        self.children = {} 
#increments the count variable with a given amount    
    def inc(self, numOccur):
        self.count += numOccur
#display tree in text. Useful for debugging        
    def disp(self, ind=1, save=[]):
        save.append('  '*ind+ self.name+ ' '+ str(self.count))
        # print ('  '*ind, self.name, ' ', self.count)
        for child in self.children.values():
            child.disp(ind+1, save = save)
def createTree(dataSet, minSup): #create FP-tree from dataset but don't mine
    headerTable = {}
    #go over dataSet twice
    for trans in dataSet:#first pass counts frequency of occurance
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]

    for k in list(headerTable):  #remove items not meeting minSup
        if headerTable[k] < minSup: 
            del(headerTable[k])
    freqItemSet = set(headerTable.keys())
    # print('freqItemSet: {}'.format(freqItemSet))
    if len(freqItemSet) == 0: return None, None  #if no items meet min support -->get out
    for k in sorted(headerTable.keys()):
        headerTable[k] = [headerTable[k], None] #reformat headerTable to use Node link 
    # print('headerTable: {}'.format(headerTable))
    retTree = treeNode('Null Set', 1, None) #create tree
    for tranSet, count in dataSet.items():  #go through dataset 2nd time
        localD = {}
        for item in tranSet:  #put transaction items in order
            if item in freqItemSet:
                localD[item] = headerTable[item][0]
        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            updateTree(orderedItems, retTree, headerTable, count)#populate tree with ordered freq itemset
    return retTree, headerTable #return tree and header table(index 1 :count, 2 :selfNode)
def updateTree(items, inTree, headerTable, count):
    if items[0] in inTree.children: #check if orderedItems[0] in retTree.children
        inTree.children[items[0]].inc(count) #incrament count
    else:   #add items[0] to inTree.children
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        # print("headerTable[items[0] : ",items[0])
        if headerTable[items[0]][1] == None: #update header table 
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:#call updateTree() with remaining ordered items
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)
def updateHeader(nodeToTest, targetNode):   #this version does not use recursion
    while (nodeToTest.nodeLink != None):    #Do not use recursion to traverse a linked list!
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode

def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        trans = sorted(trans)
        # print(str(trans).strip('frozenset()'))
        
        retDict[frozenset(trans)] = retDict.get(frozenset(trans), 0)+1
    return retDict

def ascendTree(leafNode, prefixPath): #ascends from leaf node to root
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)
def findPrefixPath(treeNode): #treeNode comes from header table
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1: 
            condPats[frozenset(prefixPath[0:])] = treeNode.count
        treeNode = treeNode.nodeLink
    return condPats
# def updateHeaderTable(dataSet, minSup, headerTable):
#     for trans in dataSet:#first pass counts frequency of occurance
#         for item in trans:
#             headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
#     print("headerTable : ", headerTable)
#     print("dataSet  : ", dataSet)
#     for k in list(headerTable):  #remove items not meeting minSup
#         if headerTable[k] < minSup: 
#             del(headerTable[k])
#     freqItemSet = set(headerTable.keys())
#     # print('freqItemSet: {}'.format(freqItemSet))
#     if len(freqItemSet) == 0: return None, None  #if no items meet min support -->get out
#     for k in headerTable:
#         headerTable[k] = [headerTable[k], None] #reformat headerTable to use Node link 