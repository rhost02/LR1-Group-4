name = "Group 4/B1"
print("Group N# & section is: " + name)

def medianValue(rawData):
    dataLength = len(rawData)
    mid = dataLength // 2
    if dataLength % 2 == 0:
        median = (rawData[mid - 1] + rawData[mid]) / 2
    else:
        median = rawData[mid]
        
    return print("The median is: ", median)
    
def meanValue(rawData):
    mean = sum(rawData) / len(rawData)
    
    return print("The mean is: ", mean)
    
def modeValue(rawData):
    mode = max(rawData,key=rawData.count)
    
    return print("The mode is: ", mode)

inputData = list(map(int, input("Enter the data: ").split()))
inputData.sort()
print('Data: ', inputData)


medianValue(inputData)
meanValue(inputData)
modeValue(inputData)