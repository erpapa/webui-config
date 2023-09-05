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
argument_parser.add_argument("--target", required=True, type=Path)
argument_parser.add_argument("--output", required=True, type=Path)
argument_parser.add_argument("--model", default="", required=False, type=str)
argument_parser.add_argument("--faces_index", default="0", required=False, type=str)
argument_parser.add_argument("--face_restorer_name", default="CodeFormer", required=False, type=str)
argument_parser.add_argument("--face_restorer_visibility", default=1.0, required=False, type=float)
argument_parser.add_argument("--upscaler_name", default="None", required=False, type=str)
argument_parser.add_argument("--upscaler_scale", default=1, required=False, type=int)
argument_parser.add_argument("--upscaler_visibility", default=1.0, required=False, type=float)
argument_parser.add_argument("--swap_in_source", default=False, required=False, type=bool)
argument_parser.add_argument("--swap_in_generated", default=True, required=False, type=bool)
argument_parser.add_argument("--nsfw_filter", default=False, required=False, type=bool)
argument_parser.add_argument("--enable", default=True, required=False, type=bool)
arguments = argument_parser.parse_args()

# Read Image
# source_bytes = io.BytesIO()
# source_img = Image.open(arguments.source).convert('RGB')
# source_img.save(source_bytes, format="PNG")
# source_data = base64.b64encode(source_bytes.getvalue())
source_file = open(arguments.source, 'rb')
source_data = base64.b64encode(source_file.read())
source_str = source_data.decode('utf-8')

# target_bytes = io.BytesIO()
# target_img = Image.open(arguments.target).convert('RGB')
# target_img.save(target_bytes, format="PNG")
# target_data = base64.b64encode(target_bytes.getvalue())
target_file = open(arguments.target, 'rb')
target_data = base64.b64encode(target_file.read())
target_str = target_data.decode('utf-8')

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
    "batch_size": 1,
    "cfg_scale": 7,
    "denoising_strength": 0.75,
    "eta": 0,
    "include_init_images": False,
    "init_images": [target_str],
    "width": target_img.width,
    "height": target_img.height,
    "inpaint_full_res": False,
    "inpaint_full_res_padding": 0,
    "inpainting_fill": 0,
    "inpainting_mask_invert": False,
    "mask": None,
    "mask_blur": 4,
    "n_iter": 1,
    "negative_prompt": "",
    "override_settings": {},
    "prompt": "",
    "resize_mode": 0,
    "restore_faces": False,
    "s_churn": 0,
    "s_noise": 1,
    "s_tmax": 0,
    "s_tmin": 0,
    "sampler_index": "Euler a",
    "seed": -1,
    "seed_resize_from_h": -1,
    "seed_resize_from_w": -1,
    "steps": 10,
    "styles": [],
    "subseed": -1,
    "subseed_strength": 0,
    "tiling": False,
    "alwayson_scripts": {
        "controlnet": {
            "args": [
                {
                    #"input_image": target_str,
                    "module": "canny",
                    "model": "control_v11p_sd15_canny [d14c016b]",
                    "weight": 1.0,
                    "processor_res": 512,
                    "threshold_a": 100,
                    "threshold_b": 200
                }
            ]
        },
        "roop": {
            "args": [
                {
                    "image": source_str,
                    "enable": arguments.enable,
                    "faces_index": arguments.faces_index,
                    "model": arguments.model,
                    "face_restorer_name": arguments.face_restorer_name,
                    "face_restorer_visibility": arguments.face_restorer_visibility,
                    "upscaler_name": arguments.upscaler_name,
                    "upscaler_scale": arguments.upscaler_scale,
                    "upscaler_visibility": arguments.upscaler_visibility,
                    "swap_in_source": arguments.swap_in_source,
                    "swap_in_generated": arguments.swap_in_generated,
                    "nsfw_filter": arguments.nsfw_filter
                }
            ]
        },
        # "roop": {
        #     "args": [
        #         source_str,
        #         arguments.enable,
        #         arguments.faces_index,
        #         arguments.model,
        #         arguments.face_restorer_name,
        #         arguments.face_restorer_visibility,
        #         arguments.upscaler_name,
        #         arguments.upscaler_scale,
        #         arguments.upscaler_visibility,
        #         arguments.swap_in_source,
        #         arguments.swap_in_generated,
        #         arguments.nsfw_filter
        #     ]
        # }
    }
}

# Send request
response = requests.post(url=f'{url}/sdapi/v1/img2img', headers=headers, json=payload)
if response.status_code != 200 :
    print(response.reason)
    sys.exit(1)

# Read results
json_data = response.json()
image_list = json_data.get('images')
if image_list is None or len(image_list) == 0:
    print("Images Not Found")
    sys.exit(1)

image_str = image_list[0]
image_data = base64.b64decode(image_str)
image_file = open(arguments.output, 'wb')
image_file.write(image_data)
