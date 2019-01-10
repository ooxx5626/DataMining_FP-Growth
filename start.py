import node_class
import file_manger
import json
from collections import defaultdict

# def newSimpDat(arr):
#     newDat = []
#     for a in arr:
#         for i in range(0,arr[a]):
#             newDat.append(a)
#     return newDat
def createInitSet(dataSet):#初始化
    retDict = {}
    for trans in dataSet:   
        retDict[frozenset(trans)] = retDict.get(frozenset(trans), 0)+1
    return retDict
def get_table(datas):#造成所需格式
    table=[]
    for tr in datas:
        for i in tr:
            if i not in table:
                table.append(i)
    return table
def loadSimpDat():#測試用投影片資料
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
# def getPattern(myHeaderTab, patterns):
    
#     for top in myHeaderTab:
#         pats = node_class.findPrefixPath(myHeaderTab[top][1])
#         # pattern = {}
#         nodeName = myHeaderTab[top][1].name
#         node_findPre_list=[]
#         for pat in pats:
#             pat_context={
#                 "pat" : clear_frozenset(pat),
#                 "count" : pats[pat]
#             }
#             node_findPre_list.append(pat_context)
#             # print(nodeName, pat)  
#         patterns[nodeName]=node_findPre_list

def clear_frozenset(string):
    return str(string).replace("frozenset({","").replace("})","").replace("'","").replace(',','').split(' ')
def checkIsexist(item, datas):#檢查有沒有存在過
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
def associate(freqItems, simpDat):
    with open("save_data/associate.txt", "w+") as f:
        rules_count = 0
        for item_i in freqItems:#分解
            for item_j in freqItems:
                if item_i != item_j:
                    item_i_count=0
                    item_j_count=0
                    if not (checkIsexist(item_i, item_j) or checkIsexist(item_j, item_i) or checkAnyexist(item_i, item_j)): #如果有存在就進入++
                        for datas in simpDat:
                            if checkIsexist(item_i, datas):
                                item_i_count += 1
                            
                            if checkIsexist(item_i, datas) and checkIsexist(item_j, datas):
                                item_j_count += 1
                        if item_i_count != 0 and item_j_count != 0 and item_j_count/item_i_count>=0.5 and item_j_count!=1:
                            print("{} >>> {}".format(item_i, item_j))
                            print("conf : {}".format(item_j_count/item_i_count))
                            f.write("{} >>> {}\n".format(item_i, item_j))#記錄起來
                            f.write("conf : {}\n".format(item_j_count/item_i_count))#記錄起來
                            rules_count +=1
        print("rules_count : {}".format(rules_count))
        f.write("rules_count : {}\n".format(rules_count))#記錄起來

def do_IBMData():
    # simpDat = loadSimpDat()
    simpDat = file_manger.readAndParser("data.ntrans_1.ascii.tlen_5.nitems_1.npats_2") #讀檔案
    table = get_table(simpDat)#建立成所需的檔案格式
    print(simpDat)
    # file_manger.save_csv(table, simpDat, 'weka_IBM.csv')#記錄起來
    # initSet = createInitSet(simpDat)
    x = []
    myFPtree, myHeaderTab = node_class.createTree(createInitSet(simpDat), 2) #建樹囉
    save = []
    myFPtree.disp(save = save)#取得顯示的東西
    for s in save:
        print(s)
    file_manger.save_tree(save, "save.txt")#記錄起來
    freqItems = []
    node_class.scanTree(myFPtree, myHeaderTab, 2, set([]), freqItems)#run過一次所需要的搜尋
    associate(freqItems, simpDat)#有多少關聯度(投影片最下面的部分)

    print(freqItems)



def do_KaggleData():
    simpDat = file_manger.readKaggle()
    file_manger.save_csv_K(simpDat[0], simpDat, 'weka_K.csv')  
    initSet = node_class.createInitSet(simpDat[1:])
    print(initSet)
    myFPtree, myHeaderTab = node_class.createTree(initSet, 10) 
    save = []
    myFPtree.show()
    file_manger.save_tree(save, "save.txt")
    freqItems = []
    node_class.mineTree(myFPtree, myHeaderTab, 10, set([]), freqItems)
    associate(freqItems, simpDat)
    print(freqItems)
do_IBMData()
# do_KaggleData()

