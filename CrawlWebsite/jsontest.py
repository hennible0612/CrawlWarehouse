import pandas as pd
import json
df = pd.read_json('\\test.json', lines=True)
print(df)
