import pandas as pd
import json
from pathlib import Path

pd.set_option('display.expand_frame_repr', False)

path = Path('./jsons')

dayton_dfs = []
virginia_dfs = []

for p in sorted(path.iterdir()):
    temp = json.load(open(p))
    path_str = str(p)
    if 'Dayton' in path_str:
        df = pd.DataFrame(temp['days'])
        dayton_dfs.append(df)
    elif 'Virginia' in path_str:
        df = pd.DataFrame(temp['days'])
        virginia_dfs.append(df)

ft_dayton_df = pd.concat(dayton_dfs, axis=0, ignore_index=True)
ft_virginia_df = pd.concat(virginia_dfs, axis=0, ignore_index=True)

ft_dayton_df.to_csv('./dayton.csv')
ft_virginia_df.to_csv('./virginia.csv')

