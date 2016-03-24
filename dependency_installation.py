import pandas as pd
import numpy as np

df = pd.DataFrame({'qty1': np.random.randn(100)})

df.to_csv('test.csv')