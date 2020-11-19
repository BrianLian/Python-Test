import time
import os
a = 12
print(time.strftime("%Y.%m.%d %H.%M.%S"))
print("print this file:\n")
now_dir = os.path.dirname(__file__)
with open(os.path.join(now_dir, '模組.py'), 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end="")
