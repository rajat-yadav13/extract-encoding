import pandas as pd
Z=pd.read_csv(r'st_data.csv')
W=Z['names'].values
R=Z['encoding'].values
#print(R)

    
def change_in_list(R):
    
    for i in range(len(W)): 
       # print(R[i])
        while 1:
            if '\n' in R[i]:
                ind = R[i].index('\n')
                R[i]=R[i][:ind]+R[i][ind+1:]
                #R[i]=R[i].split(' ')
            else:
                break
        R[i]=R[i].split(' ')
        c=R[i].count('')
        for j in range(c):
            R[i].remove('')
        R[i][0]=R[i][0][1:]    
        #print(R[i][0])
        #print(len(R[i]))
        if ']' in R[i]:
            R[i]=R[i][:len(R[i])-1]
        else:    
        #print(len(R[i][len(R[i])-1]))
            R[i][len(R[i])-1]= R[i][len(R[i])-1][:len(R[i][len(R[i])-1])-1]
        #print(R[i][len(R[i])-1])
    for i in range(len(W)):
        R[i]=list(map(float,R[i]))
        print(R[i])

    return R
print(change_in_list(R))
