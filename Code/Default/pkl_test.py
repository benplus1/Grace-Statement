# import libraries
import pickle
import json
import sys
import os

#results/Chart/Chartres0_0_0.01_60.pkl

with open('dataset/Time.pkl', 'rb') as f:
    data = pickle.load(f)


json_obj = json.loads(json.dumps(data, default=str))

with open('dataset/Time.json', 'w', encoding='utf-8') as outfile:
    json.dump(json_obj, outfile, ensure_ascii=False, indent=4)