##
## Si la columna _c0 es la clave en las tablas tbl0.tsv
## y tbl2.tsv, compute la suma de tbl2._c5b por cada
## valor en tbl0._c1.
## 

import pandas as pd
import numpy as np
df=pd.read_csv('tbl0.tsv',delimiter='\t')
dg=pd.read_csv('tbl1.tsv',delimiter='\t')
dh=pd.read_csv('tbl2.tsv',delimiter='\t')

#Respuesta
dh.groupby('_c5a')['_c5b'].sum()
