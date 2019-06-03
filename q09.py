##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 

import pandas as pd
import numpy as np
df=pd.read_csv('tbl0.tsv',delimiter='\t')
dg=pd.read_csv('tbl1.tsv',delimiter='\t')
dh=pd.read_csv('tbl2.tsv',delimiter='\t')

#Respuesta
dfax = df.groupby('_c1')['_c2'].apply(list) 
df1 = pd.DataFrame()
df1['_c1'] = dfax.keys()
df1['lista'] = [elem for elem in dfax]
df1['lista'] = [":".join(str(v) for v in sorted(elem)) for elem in df1['lista']]
df1

