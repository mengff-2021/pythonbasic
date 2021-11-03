
def spin(data,i):
    print(data,len(data),i)
    n = len(data)
    index = 0
    while index < i:
        data = spinData(data,n)
        index = index + 1
    print( "complete", data)

def spinData(data,n):
    index = 0
    temp = ""
    while index < n - 1:
        if 0 == index:
            temp = data[index]
        data[index] = data[index + 1]
        index = index+1
    data[n-1] = temp
    print(data)
    return data
    
print ("Hello world")

data = ["a","b","c","d","e","f","g","h"]
spin(data,3)
