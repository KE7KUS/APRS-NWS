#!/usr/bin/python3

import sys, os

if os.path.exists('/tmp/wxalerts.txt'):
    with open('/tmp/wxalerts.txt', 'r+') as f:
        lines = f.readines()
        if len(lines) != 0:
            sys.stdout.write(lines[0] + '\n')
            f.seek(0)
            f.truncate()
            f.writelines(lines[1:])
        elif len(lines) == 0:
            print('No alerts to process.')
        else:
            print('Unknown file length.')
    f.close()
else:
    print('No alert file to parse.')
