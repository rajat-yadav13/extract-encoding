import pandas as pd
Z=pd.read_csv(r'st_data.csv')
W=Z['names'].values
gf=['date']
for i in range(len(W)):
  gf.append(W[i])
d=pd.DataFrame(columns=gf)

d.to_csv(r'C:\Users\Asus\Desktop\att_sheet.csv',index=False)

