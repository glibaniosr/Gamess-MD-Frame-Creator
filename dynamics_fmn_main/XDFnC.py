#This is the XYZ Dynamics Framenumber Changer, or XDFnC.
#Code for change the Frame number from any sequential xyz files from a molecular dynamics.

#Functions

def copyFile(source,dest):
    import shutil
    with open(source,'r') as src, open(dest, 'w+') as dst:
        shutil.copyfileobj(src,dst)

def checkFile(fileName):
    import os
    import sys
    file = fileName
    if os.path.isfile(fileName):
        pass
    else:
        print("There is no file " + fileName + " in the directory")
        sys.exit("Ending Program")

def lineCounter(fileName):
    with open(fileName) as inputFile:
            nlines = sum(1 for _ in inputFile)
            #print(nlines)
            return nlines

def readLastFrameNumber(fileName,nlines,natoms): #dif is the number of the last frame of the file
    with open(fileName) as inputFile:
        for i, line in enumerate(inputFile):
            if i == (nlines - (natoms+1)):
                dif = int(re.search(r'\d+', line).group())
                #print(dif)
                return dif

def removeBlankLines(fileName):
    import fileinput
    for line in fileinput.FileInput(fileName,inplace=1):
        if line.rstrip():
            return

#Starting the code:
#Get the number of XYZ files
numberFiles = int(input("Type the number of XYZ files you want to mix: "))+1
#Get the name of the final unique file
finalFileName = input("\nEnter the name of the final file: ")
finalFileName = finalFileName+".xyz"

#Capture the files names
fileNumber = 1
filesList = []
while fileNumber < numberFiles :
    currentFile = input("\nType the name of xyz file number {0:d} (no extension): " .format(fileNumber))
    filesList.append(currentFile+".xyz")
    fileNumber = fileNumber + 1
for file in filesList:
    checkFile(file)

#Remove
#Start to modify the files
#First file just have to be copied to finalFile, and then can be discarded
copyFile(filesList[0],finalFileName)

#Read the number of atoms and last frame from first file
import re
with open(filesList[0]) as firstFile:
    for i, line in enumerate(firstFile):
        if i == 0:
            natoms = int(re.search(r'\d+', line).group())
            #print(natoms)

nlines = lineCounter(filesList[0])
dif = readLastFrameNumber(filesList[0],nlines,natoms)
del filesList[0]


#Substitute the frame name of the subsequential files in the desired order (one single file)
for currentFile in filesList:
    with open(currentFile) as inputFile, open(finalFileName, "a") as outputFile:
        #outputFile.writelines("\n")
        nlines = lineCounter(currentFile)
        nextDif = readLastFrameNumber(currentFile, nlines, natoms)
        lines = inputFile.readlines()
        cont = 0
        while cont < nextDif:
            i = 1+cont*(natoms+2)
            newLine = "Frame {0:d}\n" .format(cont+1 + dif)
            lines[i] = newLine
            cont +=1
        outputFile.writelines(lines)
        dif += nextDif

#with open(finalFileName) as outputFile:
#    lines = outputFile.read()
#    print(lines) 
  
  