def readAndParser(fileName):
    with open("use_data/{}".format(fileName), "r") as f:
        line = f.read(1)
        dataset = []
        newList = []
        index=''
        while line:
            # Do stuff with byte.
            line = f.readline()
            if line !='':
                lineList = line.split( )
                if lineList[0] != index:
                    index = lineList[0]
                    if len(newList)>0:
                        dataset.append(newList)
                    newList = []
                newList.append(lineList[2])
    return dataset
def readKaggle():
    fileName= "Video_Games_Sales_as_at_22_Dec_2016.csv"
    with open("use_data/{}".format(fileName), "r") as f:
        line = '0'
        # print(line)
        dataset = []
        index=''
        while line:
            # Do stuff with byte.
            line = f.readline()
            if line !='':
                data = KaggleParser(line.split(','))
                if data != '':
                    dataset.append(data)
    return dataset
def KaggleParser(line):
    isNeed = True
    for index in range(10,15):#後面全部空值
        # print(line[index])
        if line[index] is '':
            isNeed = False
            
    if isNeed:
        try:
            line[15] = line[15].replace("\n", "")
            for index in range(5,9):
                line[index] = round(float(line[index]))
            # line = line[0:4]+line[13]
        except:
            isNeed = False
    else:
        line = ''
    # print(isNeed, line)
    return line

def save_csv(table, datas, fileName):
    with open("save_data/{}".format(fileName), "w+") as f:
        # print(table)
        f.write(','.join(table))
        for item in datas:
            f.write('\n')
            line=[]
            for t in table:
                if t in item:
                    line.append("T")
                else:
                    line.append("")
            f.write(','.join(line))
def save_file(datas):
    with open("save_data/fileName.txt", "w+") as f:
        f.write(str(datas))
def save_tree(save, fileName):
    with open("save_data/{}".format(fileName), "w+") as f:
        for s in save:
            f.write(s)
            f.write("\n")
        