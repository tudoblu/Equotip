# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 08:49:03 2016

@author: ctq1
"""

import pandas as pd

'''como o arquivo pode ter espaços ou tabs, a expressão regular \s+  funciona melhor'''
header_row = ['Perfil','Sondador','Facies','Fraturas']
df = pd.read_csv('DensP21_3rjs739a_A7output.txt',sep = '\s+',skiprows = [0,1,2,3,4,5], names =header_row,usecols =[2,3])

print df