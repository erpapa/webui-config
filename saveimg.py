#!/usr/local/bin/python3

import json
import base64
from pathlib import Path
from argparse import ArgumentParser

argument_parser = ArgumentParser()
argument_parser.add_argument("--input", required=True, type=Path)
argument_parser.add_argument("--output", required=True, type=Path)
argument_parser.add_argument("--key", default="images", required=False, type=str)
arguments = argument_parser.parse_args()

json_file = open(arguments.input, 'r', encoding='utf-8')
json_data = json.load(json_file)
keys = arguments.key.split('.')
for key in keys:
    if isinstance(json_data, dict):
        json_data = json_data.get(key)
    if isinstance(json_data, list):
        json_data = json_data[0]

image_data = base64.b64decode(json_data)
image_file = open(arguments.output, 'wb')
image_file.write(image_data)
