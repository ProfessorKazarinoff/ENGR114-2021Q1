# clean_data.py

import pandas as pd
import numpy as np

def clean_data(df, w_type):
    if w_type == 'temperature':
        s = df['field4']
    elif w_type == 'pressure':
        s = df['field6']
    elif w_type == 'humidity':
        s = df['field3']
    else:
        s = df['field5']
    
    a = np.array(s)
    return a
