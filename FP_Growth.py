# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 21:24:10 2018

@author: Tony
"""

import file_manger
class treeNode:   #定義一個Tree
    def __init__(self,nameValue, numCount, parentNode):
        self.name = nameValue #紀錄item的名字
        self.count = numCount #計算次數
        self.parent = parentNode #存放節點的父節點
        self.children = {}   #存放節點的子節點
        self.nodeLink = None #連接有相關的item  
    
    def inc(self, numOccur):   #對count變數增加給定值
        self.count += numOccur
      
    def show(self, ind = 1):  #顯示Tree架構   
        print("  " * ind, self.name, "  ",self.count)
        for child in self.children.values():
            child.show(ind + 1)

def createTree(dataSet, minSup):  #構建FP-tree
    headerTable = {}
    for trans in dataSet:   #第一次scan，建item對應的次數之表格
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    for k in list(headerTable):   #將不滿足min-support的item刪除
        if headerTable[k] < minSup:
            del(headerTable[k])
    freqItemSet = set(headerTable.keys())  
    #print ('freqItemSet: ',freqItemSet)
    
    if len(freqItemSet) == 0:   #若是空item集，回傳None
        return None, None
    for k in sorted(headerTable.keys()):   #建Table，存放指向有關聯的item
        headerTable[k] = [headerTable[k], None]
    #print ('headerTable: ',headerTable)
    retTree = treeNode('Null Set', 1, None)    #初始化tree(Root)
    
    for tranSet, count in dataSet.items():  #第二次scan，建FP-tree
        localD = {}    #對一個itemset做tranSet，紀錄每個item的次數
        for item in tranSet:
            if item in freqItemSet:    #只對frequentItemset做排序
                localD[item] = headerTable[item][0]    
        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]   #排序
            updateTree(orderedItems, retTree, headerTable, count)   #更新FP-tree
    return retTree, headerTable   #回傳Tree跟表格

def updateTree(items, inTree, headerTable,count):
    if items[0] in inTree.children:   # 檢查是否存在此節點
        inTree.children[items[0]].inc(count) # 存在則count增加
     
    else:  #若不存在，則創建一個新的Treenoe並將其作為子節點加到Tree中   
        inTree.children[items[0]] = treeNode(items[0],count,inTree)    #創建新節點
        if headerTable[items[0]][1]==None:  #更新表格或前一個有關聯的item指向新節點，若原来不存在該類別，更新表格
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1],inTree.children[items[0]])
          
    if len(items) > 1: #對剩下的item迭代
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)    
            
def updateHeader(nodeToTest, targetNode):  #獲得表格中該item對應的尾節點，然後將它指向新節點(targetNode)
    while (nodeToTest.nodeLink != None):
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode   

def loadSimpDat():   #生成itemsets
    simpDat = [['Bread', 'Milk', 'Beer'],
               ['Bread', 'Coffee'],
               ['Bread', 'Egg'],
               ['Bread', 'Milk', 'Coffee'],
               ['Milk', 'Egg'],
               ['Bread', 'Egg'],
               ['Milk', 'Egg'],
               ['Bread', 'Milk', 'Egg', 'Beer'],
               ['Bread', 'Milk', 'Egg']]
    return simpDat

def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:   
        retDict[frozenset(trans)] = retDict.get(frozenset(trans), 0)+1
    return retDict

#給定itemset生成一個條件模組（前綴path）
def findPrefixPath(basePat,treeNode):   #basePat表示輸入的frequentitem，treeNode為當前FP-tree中對應的第一個節點（可在函數外部通過headerTable[basePat][1]獲得）
    condPats = {}
    while treeNode != None:
        prefixPath = []     
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1:
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink
    return condPats   #回傳函数的條件模組

def ascendTree(leafNode, prefixPath):   #輔助函數，直接修改prefixPath的值，將當前節點leafNode添加到prefixPath的尾端，然後遞歸添加其父節點
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)    
        
#遞歸查找頻繁項集
# inTree、headerTable:由createTree()函數生成的itemset的FP-tree
# minSup:表示最小支持度
# preFix:請傳入一個空集合（set([])），將在函數中用於保存當前前綴
# freqItemList:請傳入一個空列表（[]），將用來儲存生成的frequentitemset
def mineTree(inTree,headerTable,minSup,preFix,freqItemList):
    bigL = [v[0] for v in sorted(headerTable.items(), key=lambda p: str(p[1]))]
    for basePat in bigL:
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        freqItemList.append(newFreqSet)
        condPattBases = findPrefixPath(basePat, headerTable[basePat][1])
        myConTree,myHead = createTree(condPattBases, minSup)
        
        if myHead != None:
            # print('conditional tree for :', newFreqSet)
            # myConTree.show()
            mineTree(myConTree, myHead, minSup, newFreqSet, freqItemList)

def fpGrowth(dataSet, minSup=2):
    initSet = createInitSet(dataSet)
    myFPtree, myHeaderTab = createTree(initSet, minSup)
    freqItems = []
    mineTree(myFPtree, myHeaderTab, minSup, set([]), freqItems)
    return freqItems

if __name__=="__main__":
    
    #測試itemset和creat-tree
#     result = {
#   'a': lambda x: x * 5,
#   'b': lambda x: x + 7,
#   'c': lambda x: x - 2
# }['a'](1)
    # x=float("1.78")
    # x = round(x)
    # print(x)
    datas = file_manger.readKaggle()
    
    file_manger.save_file(datas)
#     simpDat = loadSimpDat()
#     initSet = createInitSet(simpDat)
#     myFPtree, myHeaderTab = createTree(initSet, 2)
#     myFPtree.show()
# #    
# #    #測試findPrefixPath
# #   
#     for index in myHeaderTab:
#         print(index,findPrefixPath('Bread', myHeaderTab[index][1]))
#     # print("z",findPrefixPath('z', myHeaderTab['z'][1]))
#     # print("r",findPrefixPath('r', myHeaderTab['r'][1]))
# #    
# #    #測試mineTree
# #    
# #    freqItems = []
# #    mineTree(myFPtree,  myHeaderTab, 2, set([]), freqItems)
# #    print(freqItems)
    
#     dataSet = loadSimpDat()
#     freqItems = fpGrowth(dataSet)
#     print(freqItems)