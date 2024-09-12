import json
import os
from functools import cache

from PIL import Image


METADATA_FILE = 'metadata.json'
TRAITS_DIR = 'traits'
OUTPUT_DIR = 'output'


@cache
def load_image(trait_type, value):
    trait_folder = next((t for t in os.listdir(TRAITS_DIR) if t == trait_type), None)
    if trait_folder is None:
        raise Exception(f'Missing folder for {trait_type}')
    trait_file = next((t for t in os.listdir(f'{TRAITS_DIR}/{trait_folder}') if t[:t.rindex('.')] == value), None)
    if trait_file is None:
        raise Exception(f'Missing image for {trait_type}/{value}')
    return Image.open(f'{TRAITS_DIR}/{trait_folder}/{trait_file}').convert('RGBA').resize((1000, 1000))


def convert_to_images():
    with open(METADATA_FILE) as f:
        metadata = json.load(f)

    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    for i, item in enumerate(metadata):
        image = None
        for attribute in item['attributes']:
            trait_image = load_image(attribute['trait_type'], attribute['value'])
            if image is None:
                image = trait_image
            else:
                image = Image.alpha_composite(image, trait_image)
        image.save(f'{OUTPUT_DIR}/{i}.webp', lossless=True)


if __name__ == '__main__':
    convert_to_images()
