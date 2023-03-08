#LR1 Group4/B1
#Prompt the user to enter input file name
inputFileName = input('Enter the input file name: ')

#Open the file for reading
fin = open(inputFileName, "r")

#Create emplty list
fileList = list()


for line in fin:
    line = line.strip('\n') 
    fileList.append(line)

cont = True
while cont:
    #Print total number of lines in file
    print('The file has',len(fileList),'lines.')
    #Prompt & read line number from file
    lineNo = int(input('Enter a line number [0 to quit]: '))
    if lineNo == 0:
        cont = False
    else:
        #Print content of line desired by user
        print(str(lineNo)+': '+fileList[lineNo-1]+'\n')

#Close file
fin.close()