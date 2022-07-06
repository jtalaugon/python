dict = {"country": ["Brazil", "Russia", "India"],
       "capital": ["Brasilia", "Moscow", "New Dehli"],
       "area": [8.516, 17.10, 3.286],
       "population": [200.4, 143.5, 1252] }

import pandas as pd
d = {(1,2),(3,4)}
df = pd.DataFrame(data=d, columns=['a','b'])
print(df)
