#!/usr/local/bin/python3

import io
import sys
import json
import base64
import requests
# from PIL import Image
from pathlib import Path
from argparse import ArgumentParser

argument_parser = ArgumentParser()
argument_parser.add_argument("--source", required=True, type=Path)
arguments = argument_parser.parse_args()

# Read Image
# source_bytes = io.BytesIO()
# source_img = Image.open(arguments.source).convert('RGB')
# source_img.save(source_bytes, format="PNG")
# source_data = base64.b64encode(source_bytes.getvalue())
source_file = open(arguments.source, 'rb')
source_data = base64.b64encode(source_file.read())
source_str = source_data.decode('utf-8')

# Request URL
url = "http://127.0.0.1:7860"

# POST headers
headers = {
    "accept": "application/json",
    "Authorization": "Basic YXBwbGU6YXBwbGU=",
    "Content-Type": "application/json"
}

# POST payload
payload = {
    "source_image": source_str,
}

# Send request
response = requests.post(url=f'{url}/roop/face_detect', headers=headers, json=payload)
if response.status_code != 200 :
    print(response.reason)
    sys.exit(1)

# Read results
json_data = response.json()
print(json_data)

