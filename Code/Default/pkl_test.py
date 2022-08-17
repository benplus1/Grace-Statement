# import libraries
import pickle
import json
import sys
import os

with open('newdataset/Chartdata.pkl', 'rb') as f:
    data = pickle.load(f)


json_obj = json.loads(json.dumps(data, default=str))

with open('newdataset/Chartdata.json', 'w', encoding='utf-8') as outfile:
    json.dump(json_obj, outfile, ensure_ascii=False, indent=4)


