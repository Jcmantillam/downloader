from logging import exception
from multiprocessing.dummy import Pool
from urllib import response
from utils import fn_timer
from urllib.request import urlretrieve
from utils import urls
import requests

@fn_timer
def requests_using_pool(urls):
    pool = Pool(20)
    resps = pool.map(download_image, urls)
    pool.close()
    pool.join()
    print(resps)
    return resps

@fn_timer
def download_using_concurrent(urls):
    for url in urls:
        download_image(url)

def main():
    filenames = []
    filenames2 = []
    print("cantidad de fotos:", len(urls))
    for image in urls:
        url_parts = image.split('/')
        name = 'images/'+ url_parts[-2] + url_parts[-1]
        name2 = 'images2/'+ url_parts[-2] + url_parts[-1]
        filenames.append(name)
        filenames2.append(name2)
    download_using_concurrent(urls)
    #requests_using_pool(urls)

def download_image(url):
    try:
        response = requests.get(url, params={})
        print(response)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        #raise SystemExit(e)

if __name__ == '__main__':
    main()
