import sys

from typing import Final
from bs4 import BeautifulSoup

USAGE: Final = "Usage: python3 penny.pyz <directory>; directory must contain index.html and index.py"

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print(USAGE)
        sys.exit(1)
