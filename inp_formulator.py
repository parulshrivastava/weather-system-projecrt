import math
import numpy as np
import pandas as pd
import re
from mat_ana import ScaleFinder
from stats_util import lmConn

class MaxzAnalyser(ScaleFinder,lmConn):  
    def __init__(self,fname,ftype):
        self.fname=fname
        self.ftype=ftype
    def dfCreater(self):
        ini=0
        fin=0
        flag=0
        file=open(self.fname,"r").read()# read
        file=file.split("\n")#new line split
        for i in file:
            if(len(re.findall('[#]',i))==0 and flag==0):
                ini+=1
            else:
                flag=1
            if(len(re.findall('[S][w][e][e][p]',i))!=0):
                break
            fin+=1
        file=file[ini:-(len(file)-fin)]#header and footer removed
        for i in range(2,len(file),3):#empty space removed
            file.remove("")
        row=file[::2]#az and el
        temp=len(row)#previous length
        datar=file[1::2]#data/intensity rows
        dc=dict()#empty dictionary for values
        if len(row)==len(datar):#row of az value only and data row of intensities
            for i in range(len(datar)):#T(n^2)
                temp=datar[i].split(' ')
                temp=list(filter(lambda x:x!='',temp))#all values in list except '' formed in above state
                temp=list(map(lambda x : np.float16(np.finfo(np.float16).min) if x=='--.-' else np.float16(x),temp))# mapping values --.- or other values
                lv=row[i].index('Az')
                hv=row[i].index('El')
                time=row[i][-10:].split(" ")
                temp1=list(filter(lambda x:x!='',row[i][lv:hv].split(" ")))
                temp1=list(map(lambda x : str(x.replace(",","")),temp1[1:]))
                temp1.append(time[-1])
                temp.reverse()
                temp.append(time[-1])
                temp.append(np.float16(temp1[1]))
                temp.append(np.float16(temp1[0]))
                temp.reverse()
                dc[i]=temp# az values as key
        col=list(range(0,len(temp)-3))#14 div right now
        col=temp1=list(map(lambda x : 'val-'+str(x+1) ,col))
        col.reverse()
        col.append('Time')
        col.append('Az-2')
        col.append('Az-1')
        col.reverse()
        dc[163]=[123,123,'34',5,0,0,np.finfo(np.float16).min,0,0,5,5,-1,0,0,0,0,0]
        df=(pd.DataFrame(dc,index=col,dtype=np.float16)).T
        df1=df
        df2=df[['Az-1', 'Az-2','Time']]
        df1.drop(['Az-1', 'Az-2','Time'],axis=1, inplace=True)
        return (df1,df2)