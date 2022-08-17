# import libraries
import pickle
import json
import sys
import os

with open('Mathres98_0_0.01_60.pkl', 'rb') as f:
    data = pickle.load(f)


json_obj = json.loads(json.dumps(data, default=str))

with open('Mathres98_0_0.01_60.json', 'w', encoding='utf-8') as outfile:
    json.dump(json_obj, outfile, ensure_ascii=False, indent=4)