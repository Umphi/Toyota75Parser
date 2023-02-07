from PIL import Image
import os
import re

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)

def compose():
    images = [
        Image.open("./imgs_o/" + f)
        for f in sorted_alphanumeric(os.listdir("./imgs_o"))
    ]

    pdf_path = "./Output.pdf"

    images[0].save(
        pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
    )

if __name__ == "__main__":
    compose()
