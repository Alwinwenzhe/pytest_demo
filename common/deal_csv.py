import csv, json, os
from contextlib import ExitStack

"""
将csv文件转换为json
"""


root_path = os.path.dirname(os.path.dirname(__file__))

def FromCsvToJson(csv_path):
    profileList = []                    # 放在函数内部，每次调用就会初始化，放在外面，会不断累加
    with open(csv_path,'r',encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            profileList.append(dict(row))
        return profileList

if __name__ == '__main__':
    print(FromCsvToJson(root_path + '/test_case/inter_case/add_step.csv'))