#!/usr/bin/env python


import requests
from sys import argv
import re

def get_processes(id):
    URL = "http://www.uniprot.org/uniprot/{}.txt".format(id)
    file_handle = requests.get(URL)
    text = file_handle.text

    match = re.findall(r"P:[^;]+;", text)
    print("\n".join([x[2:len(x)-1] for x in match]))

testvar = "P56892"
get_processes(testvar)
