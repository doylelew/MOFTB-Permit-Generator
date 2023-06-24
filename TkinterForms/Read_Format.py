import os
import json

def readFormat(format_file: str):
    with open(format_file) as file:
        format_data = json.loads(file)
    print(format_data)




