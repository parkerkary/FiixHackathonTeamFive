from Sorter import *

## The path of the folder that contains all of the image files
imageFolder = "../assets/images/"
## the path of the file containing the labels
labelFile = "../assets/labels.txt"

if __name__ == "__main__":
    fs = FileSorter.FileSorter(imageFolder,labelFile)
    fs.sort()