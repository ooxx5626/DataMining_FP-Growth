# -*- coding: utf-8 -*-
class treeNode:
    def __init__(self, nameValue, myCount, parentNode):
        self.name = nameValue #放了哪個資料
        self.count = myCount #數量
        self.nodeLink = None #不同樹的節點連結
        self.parent = parentNode #放父節點
        self.children = {} #放chlidren

    def addChild(self, child_key, node): #增加子樹
        self.children[child_key] = node
        
    def disp(self, ind=1, save=[]):#show tree
        save.append('  '*ind+ self.name+ ' '+ str(self.count))
        for child in self.children.values():
            child.disp(ind+1, save = save)

def getHeaderDict(dataSet):
    HeaderDict = {}
    for trans in dataSet:   #第一次scan，建item對應的次數之表格
        for item in trans:
            HeaderDict[item] = HeaderDict.get(item, 0) + dataSet[trans]
    return HeaderDict

def delTooLittleData(HeaderDict, minSup):
    for k in list(HeaderDict):   #將不滿足min-support的item刪除
        if HeaderDict[k] < minSup:
            del(HeaderDict[k])
    return set(HeaderDict.keys())#取出不重複的所有key

def ascendTree(leafNode, prefixPath): #從leaf爬到root
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)

def createTree(dataSet, minSup):  #構建FP-tree
    HeaderDict = getHeaderDict(dataSet)
    freqItemSet = delTooLittleData(HeaderDict, minSup)

    if len(freqItemSet) == 0:   #若資料處理完沒東西就不用處理了(ex. <min)
        return None, None
    for k in HeaderDict:   #預先新增children的位置
        HeaderDict[k] = [HeaderDict[k], None]

    retTree = treeNode('Root', 1, None)    #建立Tree的root
    if len(dataSet) > 0 or len(freqItemSet) >0: #如果他們都是0就不用做了
        for tranSet, count in dataSet.items():  #開始建tree
            nodeCount = {}    #紀錄每個item的次數
            for item in tranSet: #把每個tranSet和freqItemSet拿出來
                if item in freqItemSet:    
                    nodeCount[item] = HeaderDict[item][0]
            orderedItems = []
            for v in sorted(nodeCount.items(), key=lambda p: p[1], reverse=True):
                orderedItems.append(v[0])
            updateTree(orderedItems, retTree, HeaderDict, count)   #更新FP-tree
    return retTree, HeaderDict   #回傳Tree跟表格

def sepSubtree(treeNode): #分離每顆子樹
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1: 
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink
    return condPats

def scanTree(inTree,HeaderDict,minSup,preFix,freqList):#掃過整棵樹
    for v in sorted(HeaderDict.items(), key=lambda p: str(p[1])):
        newFreqSet = preFix.copy()
        newFreqSet.add(v[0])
        freqList.append(newFreqSet)
        condPattBases = sepSubtree(HeaderDict[v[0]][1])
        newConTree,newHead = createTree(condPattBases, minSup)
        if newHead != None:
            scanTree(newConTree, newHead, minSup, newFreqSet, freqList)

def updateTree(items, inTree, HeaderDict, count):
    item_key = items[0]
    if item_key in inTree.children: #如果被存過了就++
        inTree.children[item_key].count += count #增加children的數量
    else:   #沒被存過就新增
        inTree.children[item_key] = treeNode(item_key, count, inTree)#新增Node
        inTree.addChild(item_key, treeNode(item_key, count, inTree))
        if HeaderDict[item_key][1] == None: #把要加的Node也加進HeaderDict紀錄
            HeaderDict[item_key][1] = inTree.children[item_key]
        else:
            nodeToTest = HeaderDict[item_key][1]
            targetNode = inTree.children[item_key]
            while (nodeToTest.nodeLink != None):
                nodeToTest = nodeToTest.nodeLink
            nodeToTest.nodeLink = targetNode
    needitems = items[1::]
    if len(items) > 1 : #如果還沒跑完就繼續更新
        updateTree(needitems, inTree.children[item_key], HeaderDict, count)

    