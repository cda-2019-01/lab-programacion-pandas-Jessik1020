##
## Agregue una columna  con la suma de _c0 y _c2 a la tabla tbl0.tsv 
## 

import pandas as pd
import numpy as np
df=pd.read_csv('tbl0.tsv',delimiter='\t')
dg=pd.read_csv('tbl1.tsv',delimiter='\t')
dh=pd.read_csv('tbl2.tsv',delimiter='\t')

#Respuesta
df['suma']=(df['_c0']+df['_c2']) 