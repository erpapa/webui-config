#!/usr/local/bin/python3

import os
from PIL import Image


def traversal_files(path):
    files = []
    for item in os.scandir(path):
        if item.is_file():
            files.append(item.path)
        else:
            files.extend(traversal_files(item))
    return files


def convert_image(input_path, output_path):
    source_img = Image.open(input_path)
    ratio = 1.0 * source_img.width / source_img.height
    if ratio > 0.75:
        crop_width = source_img.height * 0.75
        crop_left = (source_img.width - crop_width) * 0.5
        print(f'Crop left: {crop_left} width: {crop_width}')
        crop_img = source_img.crop((crop_left, 0, crop_left + crop_width, source_img.height))
    elif ratio < 0.75:
        crop_height = source_img.width / 0.75
        crop_top = (source_img.height - crop_height) * 0.5
        print(f'Crop top: {crop_top} height: {crop_height}')
        crop_img = source_img.crop((0, crop_top, source_img.width, crop_top + crop_height))
    else:
        crop_img = source_img
    output_img = crop_img.resize((900, 1200), Image.BILINEAR)
    dir_name = os.path.dirname(output_path)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    output_img.save(output_path, quality=90)


# print('Traversal files.')
# files = traversal_files(os.curdir)
# print('Remove files.')
# for file in files:
#     if file.endswith('_1.png') or file.endswith('_1.jpg'):
#         os.remove(file)

print('Traversal files.')
files = traversal_files(os.curdir)
print('Convert start.')
for file in files:
    if file.endswith('png') and file.startswith('./'):
        convert_image(file, file.replace('./', './Convert/'))
        print(f'Convert file: {file}')
    elif file.endswith('jpg') and file.startswith('./'):
        convert_image(file, file.replace('./', './Convert/'))
        print(f'Convert file: {file}')

print('Convert end.')

