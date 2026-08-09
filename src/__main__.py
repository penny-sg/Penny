import sys
import penny

from typing import Final

USAGE: Final = "Usage: python3 penny.pyz <directory>; directory must contain index.html and index.py"

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print(USAGE)
        sys.exit(1)
    project_dir = args[1]
    with open(project_dir + 'index.html', 'r') as f_i:
        index = f_i.read()
    with open(project_dir + 'index.py', 'r') as f_s:
        script = f_s.read()
    print(penny.exec_files(index, script))
