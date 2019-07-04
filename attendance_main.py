
import pandas as pd
import face_recognition as fc
import cv2
import time as t
from datetime import timedelta,date,datetime
from project1_1 import change_in_list


def camera():
    Z=pd.read_csv(r'st_data.csv')
    W=Z['names'].values

    e=change_in_list(Z)
    att=[]
    for i in range(len(W)):
        att.append(0)
    v=cv2.VideoCapture(0)
           
    while True:
        r,live=v.read()
        j=live.copy()
        j=cv2.resize(live,(200,200))
        
        F=fc.face_locations(j)
        #print(F)
        if len(F)>0:
            E=fc.face_encodings(j,F)[0]
            #print(E)
            (y,x,y1,x1) = F[0] 
            cv2.rectangle(j,(x,y1),(x1,y),(0,0,255),5)
            s=fc.compare_faces(e,E)
            #print(s)
            res= True in s
            if res== True:
                att=W[s.index(True)]
                attendance(att)
        #print(att)
        cv2.imshow('my',j)
        
        k=cv2.waitKey(5000)
        if k==ord('q'):
            cv2.destroyAllWindows()
            break
    return  att     





def attendance(att):
    import datetime as d
    Z=pd.read_csv(r'st_data.csv')
    W=Z['names'].values
    gf=['date']
    
    for i in range(len(W)):
        gf.append(W[i])
    #print(gf)
    
    curr_date=d.datetime.now().strftime('%Y:%d:%B')
    R=pd.read_csv(r'C:\Users\Asus\Desktop\att_sheet.csv')
    da=R.values
    #print(da)
    arrdate=da[:,0]
    #print(arrdate)

    if curr_date not in arrdate:
        apndrow=[]
        for i in range(len(gf)):
            if i==0:
                apndrow.append(curr_date)
            else:
                apndrow.append(0)
        #da.append(apndrow) as da is array
        #print(apndrow)        
        da=np.append(da,[apndrow],axis=0)   # column should be same as row for axis to work without axis data add in other row or cl     

    da[list(arrdate).index(curr_date),gf.index(att)]=1

    newd=pd.DataFrame(da,columns=gf)
    print(newd)
    newd.to_csv(r'C:\Users\Asus\Desktop\att_sheet.csv',index=False)
    print('attandance done of',att)





def start():
    end_t=datetime.now() + timedelta(seconds= 10)
    print(end_t)
    while datetime.now()<= end_t:
        print('enter "c" for giving attendance')
        print('wait untile camera detect u')
        print('attendance marked one at a time')
        print('enter q after ur attendance is taken')
        print('attendance will only be taken in between 9:00 am to 9:30')

        g=input('enter c to start camera')
        if g=='c':
            h=camera()
        else:
            print('invalid key')

start()            
