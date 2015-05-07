#Code to change the title frame #(number) of a dynamics xyz, numbering in the order that you want

#Functions

def copyFile(source,dest):
    import shutil
    with open(source,'r') as src, open(dest, 'w+') as dst:
        shutil.copyfileobj(src,dst)


#Essa função que está dando dor de cabeça
def fileReplaceLines(inFile,outFile,dif):    
    with open(inFile) as input, open(outFile, 'a') as output :
        output.writelines("\n")
        for line in input:
            cont = 1
            while cont < dif:            
                oldString = "Frame " + str(cont)
                newString = "Frame " + str(cont + dif)                 
                line = line.replace(oldString, newString)        
                cont = cont + 1 
            output.writelines(line)
    

#checkFile checks if a File exists, and if not, it stops the execution of the program
def checkFile(fileName):
    import os
    import sys
    file = fileName
    if os.path.isfile(fileName):
        pass
    else:
        print("There is no file: " + fileName + " in the directory")
        if quitFlag:
            sys.exit("Ending Program")

#Starting the code:
#Get the number of XYZ files
numberFiles = int(input("Type the number of XYZ files you want to mix: "))+1
fileNumber = 1
filesList = []

#Get the name of the final unique file
finalFileName = input("Enter the name of the final file: ")

#Loop to get all the file names in a list (filesList)
while fileNumber < numberFiles :
    currentFile = input("Type the name of the file number {0:d}: " .format(fileNumber))
    filesList.append(currentFile)
    fileNumber = fileNumber + 1


dif = int(input("What is the last frame number of the first file? "))


for file in filesList:
    checkFile(file)
    

#Start to modify the files
for fileName in filesList :
    #Start with the firstFile, and copy its contents to a new created finalFile
    if fileName == filesList[0]:
        copyFile(filesList[0],finalFileName)                 
    else:
        fileReplaceLines(fileName,finalFileName,dif)


#See the content of the final file
with open(finalFileName) as finalFile:
    finalFile = finalFile.read()
    print(finalFile) 
