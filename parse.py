import requests
import shutil
import os
from bs4 import BeautifulSoup

def parse(carid):
    host = "https://www.toyota.co.jp/jpn/company/history/75years/vehicle_lineage/catalog/"
    for page in range(1, 50):
        for tile in range(1, 7):
            r = requests.get(f"{host}/{carid}/page{page}/x2/{tile}.jpg", stream=True)
            if r.status_code == 200:
                if not os.path.exists(f"./imgs/{page}"):
                    os.makedirs(f"./imgs/{page}")
                with open(f"./imgs/{page}/img{tile}.jpg", 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)


if __name__ == "__main__":
    parse("60002190A")
