##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 

import pandas as pd
import numpy as np
df=pd.read_csv('tbl0.tsv',delimiter='\t')
dg=pd.read_csv('tbl1.tsv',delimiter='\t')
dh=pd.read_csv('tbl2.tsv',delimiter='\t')

#Respuesta
dh['_c5'] = dh['_c5a'] + ":" + dh['_c5b'].astype('str')
dfauxi= dh.groupby('_c0')['_c5'].apply(list)
dh1 = pd.DataFrame()
dh1['_c0'] = dfauxi.keys()
dh1['lista'] = [elem for elem in dfauxi]
dh1['lista'] = [",".join(str(v) for v in sorted(elem)) for elem in dh1['lista']]
dh1