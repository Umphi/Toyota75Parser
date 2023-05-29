from multiprocessing import cpu_count, Pool
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup

import requests, shutil, os

from configloader import load_config
from requests.auth import HTTPProxyAuth

def parse_by_args(args):
    url, carid, page, tile, proxies, auth = args[0], args[1], args[2], args[3], args[4], args[5]
    r = requests.get(url, proxies=proxies, auth=auth)
    if r.status_code == 200:
        try:
            if not os.path.exists(f"./imgs/{carid}/{page}"):
                os.makedirs(f"./imgs/{carid}/{page}")
        finally:
            with open(f"./imgs/{carid}/{page}/img{tile}.jpg", 'wb') as f:
                f.write(r.content)
            return 0

def download_parallel():
    config = load_config("settings.ini")
    carid = config["Car"]["id"]
    proxies = None
    auth = None
    if config["Proxy"]["enabled"]:
        proxies = {"http": config["Proxy"]["http"], "https": config["Proxy"]["https"]}
        auth = HTTPProxyAuth(config["Proxy"]["username"], config["Proxy"]["password"])

    if not os.path.exists(f"./imgs/{carid}"):
        os.makedirs(f"./imgs/{carid}")

    cpus = cpu_count()
    data = []
    host = "https://www.toyota.co.jp/jpn/company/history/75years/vehicle_lineage/catalog"
    for page in range(1, 50):
        for tile in range(1, 7):
            data.append((f"{host}/{carid}/page{page}/x2/{tile}.jpg", carid, page, tile, proxies, auth))

    pool = Pool(cpus - 1)
    pool_answer = pool.map_async(parse_by_args, data)

    pool_answer.get()

    pool.close()
    pool.join()

def main():
    download_parallel()

if __name__ == "__main__":
    main()
