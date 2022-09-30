#dependencies: numpy, pandas and brightway2
import numpy as np
import pandas as pd
import brightway2 as bw

def all_impcats_lca(method_name):
    df=pd.DataFrame(bw.methods)
    tups=list(bw.methods)
    col0=set(df[0])
    df_methods=pd.DataFrame(index=list(col0),columns=['impact cat','tuples list'])
    for i in df_methods.index:
        impcat=set(df[1][np.where(df[0]==i)[0]])
        df_methods['impact cat'][i]={j:[df[2][k] for k in df.index if df[0][k]==i and df[1][k]==j] for j in impcat}
        df_methods['tuples list'][i]=[m for m in tups if m[0]==i]
    impcat_list=df_methods['impact cat'][method_name]    
    tups_list=df_methods['tuples list'][method_name]
    return tups_list, impcat_list
