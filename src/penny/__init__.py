import re

from bs4 import BeautifulSoup

def exec_file(in_file: str, script_file: str):
    tag_regex = re.compile(r'pnn-x-[a-z\-]+')
    soup = BeautifulSoup(in_file, 'html.parser')
    for tag in soup.find_all(teg_regex):
        fun_name = tag.name[6:].replace('-', '_')
