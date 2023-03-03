# # Practice 2

import pandas as pd

df = pd.DataFrame({'A': ['foo', 'bar', 'baz'],
                   'B': [[1, 2], [3, 4, 5], [6]]})

df = df.explode(column='B')

df.to_csv('outputs/practice2.csv', index=False)
