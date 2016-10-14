# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 20:04:51 2016

@author: paulo_000
"""
import pandas as pd

df = pd.read_csv('Pulgs_GODEL_28_01_2016.txt', sep="\t", skiprows =[0])
#----------------------------------------------------------------------------
'''retira sinal + - e string HLD da coluna Value'''
df['Value'] = df['Value'].map(lambda x: x.lstrip('+-').rstrip('HLD'))
#----------------------------------------------------------------------------
'''Cria novos dataframes chamado df1 e df2 que incluem todas as linhas onde o valor 
das células na coluna Index não é a string 'Static' (df1) e a coluna Scale não é
a string 'HLD  Leeb D' '''
df1 = df[df.Index != 'Statistic']
df2 = df1[df1.Scale != 'HLD  Leeb D']
#----------------------------------------------------------------------------
'''Retira as colunas sem dados de interesse'''
df2.drop(df2.columns[[1,2,5,6,7]], axis=1, inplace=True)
print df2
#----------------------------------------------------------------------------
'''Salva arquivo txt com as colunas de interesse'''
df2.to_csv('Pulgs_Godel_28.txt', sep='\t')

