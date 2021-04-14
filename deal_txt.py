# -*- coding:utf-8 -*-

import sys
import pandas as pd
import importlib
import io


importlib.reload(sys)


if __name__ == '__main__':
    filepath = r"E:\tim\applications\records\dai.txt" # txt源文件
    xls = pd.read_excel(r'E:\tim\applications\records\xlsx\Chat_D.xlsx', header=0)
    f = io.open(filepath, "r", encoding='utf-8')
    result_list = list()
    id = 1
    for line in f.readlines():
        line = line.strip() # 去除首尾无意义符号
        if not len(line):
            continue # 空行则跳过
        if line.startswith("[图片]"):
            continue
        if line.startswith("您好，我现"):
            continue

        if line.endswith("***"):
            status = 0
            continue
        if line.endswith("***"):
            status = 1
            continue

        xls = xls.append({'time': 0, 'status': status, 'none': 0, 'id': id, 'content': line}, ignore_index=True)
        id += 1

    f.close
    xls.to_excel(r'E:\tim\applications\records\xlsx\Chat_D.xlsx', index = False)
    print("----")