# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:27:24 2016

@author: ctq1
"""

import pandas as pd

df = pd.read_csv("Amostras_UFCG_e_BR_14-07-2015.csv", header =0)
#print df.columns #display das colunas do arquivo
df1 = df.drop(df.columns[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,23,24,25,26]],axis =1)
df2 = df1.transpose()
print df2
