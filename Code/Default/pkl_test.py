# import libraries
import pickle
import json
import sys
import os

#results/Chart/Chartres0_0_0.01_60.pkl

# with open('dataset/Closure.pkl', 'rb') as f:
#     data = pickle.load(f)


# json_obj = json.loads(json.dumps(data, default=str))

# with open('dataset/Time.json', 'w', encoding='utf-8') as outfile:
#     json.dump(json_obj, outfile, ensure_ascii=False, indent=4)

###
project_name = "Closure"

out_str = "\'Closure\':{"

with open('dataset/jsonConversions/' + project_name + '.json', 'rb') as f:
    project_json = json.load(f)

with open('dataset/Closure0001.json', 'w', encoding='utf-8') as outfile:
    json.dump(project_json[100], outfile, ensure_ascii=False, indent=4)

    # for i, proj_data in enumerate(project_json):
    #     bug_name = proj_data['proj']
    #     out_str = out_str + str(i) + ": " + bug_name[7:] + ", "

    # out_str = out_str + "}"

    # print(out_str)