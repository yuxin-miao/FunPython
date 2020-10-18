import os
import time
from datetime import datetime


def pressSpace():
    with open("filename", 'r') as f:
        code = ''
        for line in f.readlines():
            code += line.lstrip()

        for i in code:
            if i == '\'' or i == '\"':
                cmd = """
                osascript -e 'tell application "System Events" to keystroke "\\{}"'
                """.format(i)
                os.system(cmd)
            elif i == '\n' or i == '\r':
                cmd = """
                osascript -e 'tell application "System Events" to key code {}'
                """.format(36)
                os.system(cmd)
            else:
                cmd = """
                osascript -e 'tell application "System Events" to keystroke "{}"'
                """.format(i)
                os.system(cmd)


if __name__ == '__main__':
    time.sleep(3)
    pressSpace()
    time.sleep(1)
