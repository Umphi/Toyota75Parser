from PIL import Image

import os, re

from configloader import load_config

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)

def compose(carid):
    images = [
        Image.open(f"./imgs_full/{carid}/" + f)
        for f in sorted_alphanumeric(os.listdir(f"./imgs_full/{carid}"))
    ]
    if not os.path.exists(f"./PDF"):
        os.makedirs(f"./PDF")
    images[0].save(
        f"./PDF/{carid}.pdf", "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
    )

def main():
    config = load_config("settings.ini")
    carid = config["Car"]["id"]
    compose(carid)

if __name__ == "__main__":
    main()
