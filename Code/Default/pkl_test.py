# import libraries
import pickle
import json
import sys
import os
import pandas as pd

file_name = "dataset/missing_lans/Lang.pkl"
objects = pd.read_pickle(file_name)

# Opening JSON file
f = open('dataset/Lang_lans_manual.json')

print(len(objects))
# returns JSON object as 
# a dictionary
data = json.load(f)

for (pkl_obj, json_obj) in zip(objects, data):
    assert pkl_obj['proj'] == json_obj['proj']
    assert len(json_obj['lans']) != 0
    print(pkl_obj['lans'])
    print(json_obj['lans'])
    pkl_obj['lans'] = json_obj['lans']

with open('dataset/Lang.pkl', 'wb') as handle:
    pickle.dump(objects, handle, protocol=pickle.HIGHEST_PROTOCOL)

# open pickle file
# with open('dataset/Mockito_lans_manual.json', 'rb') as infile:
#     obj = json.load(infile)

# with open('dataset/Mockito.pkl', 'wb') as handle:
#     pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)
    # with open('dataset/Closure.pkl', 'rb') as f:
#     data = pickle.load(f)

# max_lines_id = 0
# max_methods_id = 0

# for i in data:
#     lines_len = len(i['lines'])
#     methods_len = len(i['methods'])
#     max_lines_id = max(max_lines_id, lines_len)
#     max_methods_id = max(max_methods_id, methods_len)

# print(max_lines_id)
# print(max_methods_id)

# json_obj = json.loads(json.dumps(data, default=str))

# with open('dataset/Time.json', 'w', encoding='utf-8') as outfile:
#     json.dump(json_obj, outfile, ensure_ascii=False, indent=4)

##
# project_name = "Closure"

# out_str = "\'Closure\':{"

# with open('dataset/jsonConversions/' + project_name + '.json', 'rb') as f:
#     project_json = json.load(f)

# with open('dataset/Closure0001.json', 'w', encoding='utf-8') as outfile:
#     json.dump(project_json[100], outfile, ensure_ascii=False, indent=4)

    # for i, proj_data in enumerate(project_json):
    #     bug_name = proj_data['proj']
    #     out_str = out_str + str(i) + ": " + bug_name[7:] + ", "

    # out_str = out_str + "}"

    # print(out_str)