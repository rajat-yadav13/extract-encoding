import os
import numpy as np
import pandas as pd
from path_extraction import getListOfFiles
import face_recognition as fc



dirName = r'C:\Users\Asus\Desktop\candid';
 
# Get the list of all files in directory tree at given path
listOfFiles,v = getListOfFiles(dirName)
#print(listOfFiles)

img=[]
    
for i in range(len(listOfFiles)):
    q=fc.load_image_file(listOfFiles[i])
    
    #print(q)
    f=fc.face_locations(q)
    #print(f)
    e=fc.face_encodings(q,f)[0]
    img.append(e)
#print(img)
#print(len(img))
p=[]

for j in range(len(v)):
    p.append([v[j],img[j]])
    
print(p)
d=pd.DataFrame(p, columns=['names','encoding'])
print(d)
d.to_csv(r'st_data.csv')
#print(pd.read_csv(r'st_data.csv'))
print('succefull file updation')

