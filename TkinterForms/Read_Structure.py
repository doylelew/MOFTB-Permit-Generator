import os
import json

def readFormat(format_json_file: str):
    with open(format_json_file) as json_file:
        format_data = json.loads(json_file.read())

    print(format_data)