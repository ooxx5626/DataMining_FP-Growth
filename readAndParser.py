def readAndParser(fileName):
    with open(fileName, "r") as f:
        line = f.read(1)
        dataset = []
        while line:
            # Do stuff with byte.
            line = f.readline()
            if(line !=''):
                dataset.append(line.split( ))
    return dataset