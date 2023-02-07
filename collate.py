from PIL import Image
import os

def collate():
    pagecount = len(os.listdir("./imgs")) + 1
    width, height = Image.open('./imgs/1/img1.jpg').size
    for imagename in range(1,pagecount):
        img = Image.new('RGB', (width*2, height*3))
        img1 = Image.open(f'./imgs/{imagename}/img1.jpg')
        img2 = Image.open(f'./imgs/{imagename}/img2.jpg')
        img3 = Image.open(f'./imgs/{imagename}/img3.jpg')
        img4 = Image.open(f'./imgs/{imagename}/img4.jpg')
        img5 = Image.open(f'./imgs/{imagename}/img5.jpg')
        img6 = Image.open(f'./imgs/{imagename}/img6.jpg')

        img.paste(img1, (0,0))
        img.paste(img2, (width,0))
        img.paste(img3, (0,height))
        img.paste(img4, (width,height))
        img.paste(img5, (0,height*2))
        img.paste(img6, (width,height*2))

        if not os.path.exists("./imgs_o"):
            os.makedirs("./imgs_o")
        img.save(f"./imgs_o/{imagename}.jpg")

if __name__ == "__main__":
    collate()
