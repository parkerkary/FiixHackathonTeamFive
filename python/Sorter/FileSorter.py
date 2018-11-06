import os

class FileSorter:

    def __init__(self, imageFolder, labelFile):
        print("Initializing Sorter")
        self.imageFolder = imageFolder
        self.labelFile = labelFile

    def sort(self):
        fp = open(self.labelFile)
        for i, lineValue in enumerate(fp):
            lineNumber = i + 1
            labelDir = self.imageFolder + str(lineValue) + "/"
            labelDir = self.mkdir(labelDir)
            currentPath = self.imageFolder + self.padNumber(lineNumber) + ".jpg"
            newPath = labelDir[:-2] + "/" + self.padNumber(lineNumber) + ".jpg"
            print(currentPath,newPath)
            os.rename(currentPath,newPath)
        fp.close()
    
    def checkDirExists(self,filepath):
        print("checking: "+ filepath)
        try:
            print(os.stat(filepath))
            return True
        except :
            return False

    def mkdir(self,filepath):
        print(self.checkDirExists(filepath))
        if(not self.checkDirExists(filepath)):
            os.mkdir(filepath)
        return filepath

    def padNumber(self,number):
        numStr = str(number)
        while(len(numStr) < 6):
            numStr = "0" + numStr
        return numStr