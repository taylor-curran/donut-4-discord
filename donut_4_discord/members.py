import pandas as pd
import numpy as np

def get_pairs(members):

    df = pd.DataFrame({'members': members})
    df_rand = df.sample(frac=1)
    # reset index

    odd = [i for i in df.index if i % 2 != 0]
    even = [i for i in df.index if i % 2 == 0]

    pairs = []
    for i in range(len(odd)):

        # DUH AttributeError: 'list' object has no attribute 'iloc'
        pairs.append([.iloc[i], even.iloc[i]])

    return pairs



toy_df = df = pd.DataFrame({'members': ['tay', 'joe', 'mo', 'tier', 'alex']})




