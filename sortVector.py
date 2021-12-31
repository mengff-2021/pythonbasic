def sortVector(data,n):
    print(data,n)
    i = 0
    k = 0
    while i < n:
        if data[i] == 1:
            k = k+1
        i = i + 1
    i = 0
    while i < k:
        data[i] = 1
        i=i+1
    while k < n:
        data[k] = 2
        k = k + 1
    print(data,n)
#a = [1,1,1,2,1,2,1,2,2,1]
#sortVector(a,len(a))

def sortData(data,n,m):
    i = 0
    k = 0
    equalData = [];
    while k < m:
       equalData.append(0)
       k = k + 1
    while i < n:
        key = data[i]
        equalData[key] =  equalData[key] + 1
        i = i + 1
    print(equalData)
    return equalData

def sortLess(data,n,m):
    i = 1
    k = 0
    lessData = [];
    while k < m:
       lessData.append(0)
       k = k + 1
    while i < n:
       lessData[i] = data[i-1] + lessData[i-1]
       i = i + 1
    print(lessData)
    return lessData


def sortInfo(data,n,m,lessData):
    k = 0
    out = [];
    while k < n:
       out.append(0)
       k = k + 1
    k = 0
    index = 0
    while k < n:
        key = data[k]
        index = lessData[key]
        out[index] = data[k]
        lessData[key]= lessData[key]+1
        k = k + 1
    print(out)

a = [4,1,5,0,1,6,2,1,5,1,5,3]
data = sortData(a,len(a),7)
lessData = sortLess(data,len(data),7)
sortInfo(a,len(a),7,lessData)

