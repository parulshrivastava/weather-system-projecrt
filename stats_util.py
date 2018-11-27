import math
import numpy as np
import pandas as pd
class lmConn:
    def pathFind(self,temp):
        (row,col)=temp.shape
        temp1=pd.DataFrame(np.full((row,col),7),columns=list(temp.columns),dtype=np.float16)
        for rowite in range(row):
            colite=col-1
            while(colite>=0):
                if(temp.iloc[rowite,colite]==np.finfo(np.float16).min):
                    temp1.iloc[rowite,colite]=-1
                elif(temp.iloc[rowite,colite-1]==np.finfo(np.float16).min):
                    temp1.iloc[rowite,colite]=-1
                else:
                    temp1.iloc[rowite,colite]=1
                colite-=1
        return temp1