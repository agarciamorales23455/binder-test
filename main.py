import numpy as np
import pandas as pd

x = np.arange(1,11,1)
y = x**2
index = range(0,10,1)
df =pd.DataFrame(data=list(zip(x,y)), index=index, columns=['x','y'])
                  
print(df.to_string())