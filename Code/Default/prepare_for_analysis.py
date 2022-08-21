# import libraries
import pickle
import json
import sys
import os

project_name = "Time"

with open('dataset/jsonConversions/' + project_name + '.json', 'rb') as f:
    project_json = json.load(f)


with open('results/' + project_name + '/' + project_name + 'res_0_0.01_60.pkl', 'rb') as g:
    data = pickle.load(g)

results_json = json.loads(json.dumps(data, default=str))

# print(len(results_json))
# print(len(project_json))
assert len(results_json) == len(project_json)

write_data = {}

for i, proj_data in enumerate(project_json):
    bug_name = proj_data['proj']
    bug_lans = proj_data['lans']
    best_epoch_results = results_json[str(i)][1]
    write_data[bug_name] = {"lans" : bug_lans, "labels" : best_epoch_results}

with open('outputs/' + project_name + '_results.json', 'w', encoding='utf-8') as outfile:
    write_json = json.loads(json.dumps(write_data, default=str))
    json.dump(write_json, outfile, ensure_ascii=False, indent=4)