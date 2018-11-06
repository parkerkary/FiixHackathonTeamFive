import os

class FileSorter:

    imageFolder = ""
    labelFile = ""

    def __init__(self):
        print("Initializing Sorter")

    def sort(self):
        fp = open(self.labelFile)
        for i, lineValue in enumerate(fp):
            lineNumber = i + 1
            print(self.padNumber(lineNumber))
            print(lineValue)
    
    def checkDirExists(self,filepath):
        try:
            os.stat(filepath)
            return True
        except :
            return False

    def mkdir(self,filepath):
        if(not self.checkDirExists(filepath)):
            os.mkdir(filepath)

    def padNumber(self,number):
        numStr = str(number)
        while(len(numStr) < 4):
            numStr = "0" + numStr
        return numStr