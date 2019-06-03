##
## Agregue el año como una columna a la tabla tbl0.tsv 
## 

import pandas as pd
import numpy as np
df=pd.read_csv('tbl0.tsv',delimiter='\t')
dg=pd.read_csv('tbl1.tsv',delimiter='\t')
dh=pd.read_csv('tbl2.tsv',delimiter='\t')

#Respuesta
df['ano'] = df['_c3'].str.split('-', 1, expand=True)[0] 