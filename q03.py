##
## Imprima el maximo de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 

import pandas as pd
import numpy as np
df=pd.read_csv('tbl0.tsv',delimiter='\t')
dg=pd.read_csv('tbl1.tsv',delimiter='\t')
dh=pd.read_csv('tbl2.tsv',delimiter='\t')

# Respuesta
df.groupby('_c1').mean()['_c2']
