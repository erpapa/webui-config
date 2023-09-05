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
argument_parser.add_argument("--target", required=True, type=str)
argument_parser.add_argument("--output", required=True, type=str)
argument_parser.add_argument("--model", default="", required=False, type=str)
argument_parser.add_argument("--faces_index", default="0", required=False, type=str)
argument_parser.add_argument("--face_restorer_name", default="CodeFormer", required=False, type=str)
argument_parser.add_argument("--face_restorer_visibility", default=1.0, required=False, type=float)
argument_parser.add_argument("--upscaler_name", default="None", required=False, type=str)
argument_parser.add_argument("--upscaler_scale", default=1, required=False, type=int)
argument_parser.add_argument("--upscaler_visibility", default=1.0, required=False, type=float)
argument_parser.add_argument("--nsfw_filter", default=False, required=False, type=bool)
arguments = argument_parser.parse_args()

# Read Image
# source_bytes = io.BytesIO()
# source_img = Image.open(arguments.source).convert('RGB')
# source_img.save(source_bytes, format="PNG")
# source_data = base64.b64encode(source_bytes.getvalue())
source_file = open(arguments.source, 'rb')
source_data = base64.b64encode(source_file.read())
source_str = source_data.decode('utf-8')

target_images = []
target_files = arguments.target.split(",")
for file in target_files:
    # target_bytes = io.BytesIO()
    # target_img = Image.open(file).convert('RGB')
    # target_img.save(target_bytes, format="PNG")
    # target_data = base64.b64encode(target_bytes.getvalue())
    target_file = open(file, 'rb')
    target_data = base64.b64encode(target_file.read())
    target_str = target_data.decode('utf-8')
    target_images.append(target_str)

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
    "target_images": target_images,
    "model": arguments.model,
    "faces_index": arguments.faces_index,
    "face_restorer_name": arguments.face_restorer_name,
    "face_restorer_visibility": arguments.face_restorer_visibility,
    "upscaler_name": arguments.upscaler_name,
    "upscaler_scale": arguments.upscaler_scale,
    "upscaler_visibility": arguments.upscaler_visibility,
    "nsfw_filter": arguments.nsfw_filter
}

# Send request
response = requests.post(url=f'{url}/roop/batch_swap_face', headers=headers, json=payload)
if response.status_code != 200 :
    print(response.reason)
    sys.exit(1)

# Read results
json_data = response.json()
json_images = json_data.get('images')
if json_images is None or len(json_images) == 0:
    print("Image Not Found")
    sys.exit(1)

output_files = arguments.output.split(",")
min_length = min(len(json_images), len(output_files))
for index in range(min_length):
    image_str = json_images[index]
    image_data = base64.b64decode(image_str)
    image_file = open(output_files[index], 'wb')
    image_file.write(image_data)
