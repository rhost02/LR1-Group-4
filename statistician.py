name = "Group 4/B1"
print("Group N# & section is: " + name)

def meanValue(rawData):
  mean = sum(rawData)/len(rawData)
  
  return print("The mean is: ", mean)

inputData = list(map(int, input("Enter the data: ").split()))
inputData.sort()
print("Data: ", inputData)

meanValue(inputData):
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
