import sys
import pandas as pd


File = sys.argv[1]


Input = pd.read_csv(File,sep="\t")      

ll=[]

for i in range(0,len(Input)):
    for j in range(1,21):
        if Input.iloc[i,j] == 9 or Input.iloc[i,j] == 6 or Input.iloc[i,j] == 7:
            ll.append(i)



Input = Input.drop(ll)



Input.to_csv('test.csv',index=False)  
