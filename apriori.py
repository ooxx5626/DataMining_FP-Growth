import sys

def getCount(D, keys):#計算每個key得數量
	Count_list = []
	for key in keys:
		count = 0
		for T in D:
			have = True
			for k in key:
				if k not in T:
					have = False
			if have:
				count += 1
		Count_list.append(count)
	return Count_list

def getCutKeys(keys, C, minSup, length):#把每次小於min的刪掉
	for i, key in enumerate(keys):
		if float(C[i]) / length < minSup:
			keys.remove(key)
	return keys

def start(Data, minSup):
	C1 = {}
	for T in Data:#把每一個資料解開
		for I in T:
			if I in C1:
				C1[I] += 1 #計算數量
			else:
				C1[I] = 1

	print(C1)
	_keys1 = C1.keys()

	keys1 = []
	for i in _keys1:
		keys1.append([i])

	n = len(Data)
	cutKeys1 = []
	for k in keys1[:]:
		if C1[k[0]]*1.0/n >= minSup:#檢查大小有沒有大於min
			cutKeys1.append(k)
	cutKeys1.sort()


	keys = cutKeys1
	all_keys = []
	while keys != []:
		C = getCount(Data, keys)
		cutKeys = getCutKeys(keys, C, minSup, len(Data))#把每次小於min的刪掉
		for key in cutKeys:
			all_keys.append(key)
		keys = aproiri_gen(cutKeys)#重新整理

	return all_keys


def aproiri_gen(keys1):#重新整理
	keys2 = []
	for k1 in keys1:
		for k2 in keys1:
			if k1 != k2:
				key = []
				for k in k1:
					if k not in key:
						key.append(k)
				for k in k2:
					if k not in key:
						key.append(k)
				key.sort()
				if key not in keys2:
					keys2.append(key)
			
	return keys2


