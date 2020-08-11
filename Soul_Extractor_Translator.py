import tkinter as tk
from tkinter import filedialog

import os
import json
import pandas as pd

root = tk.Tk()
root.withdraw()
root.call('wm', 'attributes', '.', '-topmost', True)
filename = filedialog.askopenfilename()


with open(filename) as raw_data:
    data=json.load(raw_data)

random_junk = data[0]
data.remove(random_junk)
json_data = pd.DataFrame(data)

print(os.listdir())
name_mapper = pd.read_csv(r'Soul_Name_Mapper.csv')

joined_data = pd.merge(left=json_data, right=name_mapper, how='left', left_on='御魂类型', right_on='EngName')
joined_data['御魂类型'] = joined_data['CNName']
joined_data = joined_data.drop(['CNName','EngName'], axis=1)

final_list = joined_data.T.apply(lambda x: x.dropna().to_dict()).tolist()
final_list.insert(0, random_junk)

with open(filename, 'w') as raw_data:
    json.dump(final_list,raw_data, indent=3)
