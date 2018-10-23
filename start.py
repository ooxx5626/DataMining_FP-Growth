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
# # print(Fre_pattern)s
