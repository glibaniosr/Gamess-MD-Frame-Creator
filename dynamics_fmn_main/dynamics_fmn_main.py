#Code to change the title frame #(number) of a dynamics xyz, numbering in the order that you want. You can use for multiple files

#Functions

def copyFile(source,dest):
    import shutil
    with open(source,'r') as src, open(dest, 'w+') as dst:
        shutil.copyfileobj(src,dst)



def fileReplaceLines(inFile,outFile,dif):    
    import re
    with open(inFile) as input, open(outFile, 'a') as output :
        output.writelines("\n")
        for line in input:
            cont = 1
            while cont < dif:                            
                oldString = "Frame {0:d}" .format(cont)
                newString = "Frame {0:d}" .format(cont + dif)            
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
#Get the name of the final unique file
finalFileName = input("Enter the name of the final file: ")

#Loop to get all the file names in a list (filesList) and all the diferences in frames
fileNumber = 1
difNumber = 1
filesList = []
difsList = []

while fileNumber < numberFiles :
    if fileNumber == numberFiles-1:
        currentFile = input("\nType the name of the file number {0:d}: " .format(fileNumber))
        filesList.append(currentFile)
    else:    
        currentFile = input("\nType the name of the file number {0:d}: " .format(fileNumber))
        filesList.append(currentFile)
        currentDif = int(input("\nWhat is the last frame number of the current file \nadded to the last frame number of all the previous files? "))
        difsList.append(currentDif)
    
    fileNumber = fileNumber + 1

for file in filesList:
    checkFile(file)
    

#Start to modify the files
#First file just have to be copied to finalFile, and then can be discarded
copyFile(filesList[0],finalFileName)
del filesList[0]
#Do the thing for the other files
for fileName,dif in zip(filesList,difsList):
    dif = int(dif)
    fileReplaceLines(fileName,finalFileName,dif)


#See the content of the final file
with open(finalFileName) as finalFile:
    finalFile = finalFile.read()
    print(finalFile) 
