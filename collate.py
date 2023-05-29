from PIL import Image
import os
from configloader import load_config

def collate(carid):
    pagecount = len(os.listdir(f"./imgs/{carid}")) + 1
    width, height = Image.open(f'./imgs/{carid}/1/img1.jpg').size
    for imagename in range(1,pagecount):
        img = Image.new('RGB', (width*2, height*3))
        for tilenum in range(1,7):
            tile = Image.open(f'./imgs/{carid}/{imagename}/img{tilenum}.jpg')
            img.paste(tile, ( width if tilenum % 2 == 0 else 0 , (tilenum - 1) // 2 * height))

        if not os.path.exists(f"./imgs_full/{carid}"):
            os.makedirs(f"./imgs_full/{carid}")
        img.save(f"./imgs_full/{carid}/{imagename}.jpg")

def main():
    config = load_config("settings.ini")
    carid = config["Car"]["id"]
    collate(carid)

if __name__ == "__main__":
    main()
