##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
## 

import pandas as pd
import numpy as np
df=pd.read_csv('tbl0.tsv',delimiter='\t')
dg=pd.read_csv('tbl1.tsv',delimiter='\t')
dh=pd.read_csv('tbl2.tsv',delimiter='\t')

#Respuesta
dfaux = dg.groupby('_c0')['_c4'].apply(list)
dg1= pd.DataFrame()
dg1['_c0'] = dfaux.keys()
dg1['lista'] = [elem for elem in dfaux]
dg1['lista'] = [",".join(str(v) for v in sorted(elem)) for elem in dg1['lista']]
dg1