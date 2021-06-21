#!/usr/bin/python3

import sys

try:
    with open('/tmp/wxalerts.txt', 'r+') as f:
        lines = f.readlines()
        sys.stdout.write(lines[0] + '\n')
        f.seek(0)
        f.truncate()
        f.writelines(lines[1:])                  
except:
    pass
