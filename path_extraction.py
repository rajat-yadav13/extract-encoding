import os
import numpy as np
import pandas as pd
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    #print(listOfFile)
   
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        #print(fullPath)
        allFiles = np.append(allFiles,os.path.join(fullPath,os.listdir(fullPath)[0]))
                   
    return allFiles,listOfFile
