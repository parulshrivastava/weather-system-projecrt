import math
import numpy as np
import pandas as pd
# coding: utf-8

# In[ ]:


class ScaleFinder:
    def lMaxima(self,temp):#T(n)=n(n+n)
        (row,col)=temp.shape
        temp1=pd.DataFrame(np.full((row,col),7),columns=list(temp.columns),dtype=np.float16)
        for rowite in range(row):
            colite=0
            while(colite<col):
                if((colite+1)<col and temp.iloc[rowite,colite]>=temp.iloc[rowite,colite+1]):
                    lv=colite
                    while(((colite+1)<col) and (temp.iloc[rowite,colite]==temp.iloc[rowite,colite+1])):
                        colite+=1
                    if(lv==0 and (colite+1)<col and temp.iloc[rowite,colite+1]<temp.iloc[rowite,colite]):
                        temp1.iloc[rowite,lv:colite+1]=np.full(len(temp1.iloc[rowite,lv:colite+1]),2)
                    elif(lv!=0 and (colite+1)==col and temp.iloc[rowite,lv-1]<temp.iloc[rowite,lv]):
                        temp1.iloc[rowite,lv:colite+1]=np.full(len(temp1.iloc[rowite,lv:colite+1]),2)
                    elif(lv!=0 and ((colite+1)!=col)):
                        if(temp.iloc[rowite,lv-1]<temp.iloc[rowite,lv] and temp.iloc[rowite,colite+1]<temp.iloc[rowite,colite]):
                            temp1.iloc[rowite,lv:colite+1]=np.full(len(temp1.iloc[rowite,lv:colite+1]),2)
                if((colite+1)==col and temp.iloc[rowite,colite]>temp.iloc[rowite,colite-1]):
                    temp1.iloc[rowite,colite]=2
                colite+=1
        return (temp1)
    def lMinima(self,temp,temp1):
        (row,col)=temp.shape
        temp2=pd.DataFrame(np.full((row,col),7),columns=list(temp.columns),dtype=np.float16)
        for rowite in range(row):
            colite=0
            flag=0
            while(colite<col):
                if(temp1.iloc[rowite,colite]==2):
                    flag=0
                    lv=-1
                    hv=-1
                if(temp.iloc[rowite,colite]==np.finfo(np.float16).min):
                    flag=1
                    lv=-1
                    hv=-1
                if(flag==0 and temp1.iloc[rowite,colite]!=2 and (colite+1)<col):
                    if(temp.iloc[rowite,colite]<temp.iloc[rowite,colite-1] and temp.iloc[rowite,colite]<temp.iloc[rowite,colite+1]):
                        temp2.iloc[rowite,colite]=0
                    elif(temp.iloc[rowite,colite]<temp.iloc[rowite,colite-1] and temp.iloc[rowite,colite]==temp.iloc[rowite,colite+1]):
                        lv=colite
                    elif(temp1.iloc[rowite,colite]!=2 and temp.iloc[rowite,colite]==temp.iloc[rowite,colite+1]):
                        hv=colite
                    elif((colite+1)<col and temp.iloc[rowite,colite]<temp.iloc[rowite,colite+1]):
                        if(lv!=-1 and hv!=-1):
                            temp2.iloc[rowite,lv:hv+2]=np.full(len(temp2.iloc[rowite,lv:hv+2]),0)
                        elif(hv==-1 and lv!=-1):
                            temp2.iloc[rowite,lv:lv+2]=np.full(len(temp2.iloc[rowite,lv:lv+2]),0)
                colite+=1
        return (temp2)
    def findCombined(self,df1,df2,df3):
        (row,col)=df1.shape
        df6=df2.copy()
        for rowite in range(row):
            for colite in range(col):
                if(df2.iloc[rowite,colite]==1 and df1.iloc[rowite,colite]==2):
                    df6.iloc[rowite,colite]=2
                elif(df2.iloc[rowite,colite]==1 and df3.iloc[rowite,colite]==0):
                    df6.iloc[rowite,colite]=0
        return df6