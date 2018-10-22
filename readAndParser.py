def readAndParser(fileName):
    with open(fileName, "r") as f:
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