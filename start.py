import node_class
import file_manger
import json
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

def get_table(datas):
    table=[]
    for tr in datas:
        for i in tr:
            if i not in table:
                table.append(i)
    return table
def getPattern(myHeaderTab, patterns):
    
    for top in myHeaderTab:
        pats = node_class.findPrefixPath(myHeaderTab[top][1])
        # pattern = {}
        nodeName = myHeaderTab[top][1].name
        node_findPre_list=[]
        for pat in pats:
            pat_context={
                "pat" : clear_frozenset(pat),
                "count" : pats[pat]
            }
            node_findPre_list.append(pat_context)
            # print(nodeName, pat)  
        patterns[nodeName]=node_findPre_list

def clear_frozenset(string):
    return str(string).replace("frozenset({","").replace("})","").replace("'","").replace(',','').split(' ')
def checkIsexist(item, datas):
    exist_count = 0
    isexist = False
    for i in item:
        if i in datas :
            exist_count+=1
    if exist_count == len(item):
        isexist=True
    return isexist
    
def checkAnyexist(item_i, item_j):
    isexist = False
    for i in item_i:
        for j in item_j:
            if i == j:
                isexist = True
    return isexist
simpDat = loadSimpDat()                             
# simpDat = file_manger.readAndParser("data.ntrans_1.ascii.tlen_5.nitems_1.npats_2")
table = get_table(simpDat) 
file_manger.save_csv(table, simpDat, 'weka.csv')  
initSet = node_class.createInitSet(simpDat)
myFPtree, myHeaderTab = node_class.createTree(initSet, 2) 
save = []
myFPtree.disp(save = save)
for s in save:
    print(s)
freqItems = []
node_class.mineTree(myFPtree, myHeaderTab, 2, set([]), freqItems)
for item_i in freqItems:
    for item_j in freqItems:
        if item_i != item_j:
            item_i_count=0
            item_j_count=0
            if not (checkIsexist(item_i, item_j) or checkIsexist(item_j, item_i) or checkAnyexist(item_i, item_j)):
                for datas in simpDat:
                    if checkIsexist(item_i, datas):
                        item_i_count += 1
                    
                    if checkIsexist(item_i, datas) and checkIsexist(item_j, datas):
                        item_j_count += 1
                if item_i_count != 0 and item_j_count != 0 and item_j_count/item_i_count>=0.5 and item_j_count!=1:
                    print(item_i," >>> ", item_j)
                    print("item_i_count :", item_i_count)
                    print("item_j_count :", item_j_count)
                    print("conf :", item_j_count/item_i_count)

print(freqItems)
# patterns={}
# getPattern(myHeaderTab, patterns)

# for item in patterns:
#     if patterns[item] !=[]:
#         print("item : ",item)
#         each_frequent_pattern = {}
#         for index in patterns[item]:
#             print("patterns[item][index] : ", index)
#             for pat in index['pat']:
#                 each_frequent_pattern[pat] =  each_frequent_pattern.get(pat, 0) + index["count"]
#         print(each_frequent_pattern)
# # print(Fre_patte