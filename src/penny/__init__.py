import re

from bs4 import BeautifulSoup

def exec_files(in_file: str, script_file: str) -> str:
    script_ns = {}
    exec(script_file, script_ns)
    
    tag_regex = re.compile(r'pnn-[a-z\-]+')
    soup = BeautifulSoup(in_file, 'html.parser')
    for tag in soup.find_all(teg_regex):
        fun_name = tag.name[4:].replace('-', '_')
        func = script_ns.get(fun_name)
        if callable(func):
            tag.replace_with(func())
        else:
            tag.extract()
    return str(soup)
