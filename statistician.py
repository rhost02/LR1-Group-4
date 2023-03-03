def meanValue(rawData):
  mean = sum(rawData)/len(rawData)
  
  return print("The mean is: ", mean)

inputData = list(map(int, input("Enter the data: ").split()))
inputData.sort()
print("Data: ", inputData)

meanValue(inputData)
