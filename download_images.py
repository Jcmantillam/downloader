from logging import exception
from multiprocessing.dummy import Pool
from utils import fn_timer
from urllib.request import urlretrieve
from utils import urls

@fn_timer
def download_using_pool(urls, filenames):
    pool = Pool(20)
    resps = pool.starmap(urlretrieve, zip(urls, filenames))
    pool.close()
    pool.join()
    return resps

@fn_timer
def download_using_concurrent(urls, filenames):
    for image_info in zip(urls, filenames):
        download_image(image_info[0], image_info[1])

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
    download_using_concurrent(urls, filenames2)
    download_using_pool(urls, filenames)

def download_image(url, filename):
    try:
        urlretrieve(url, filename)
    except exception as e:
        print(e)

if __name__ == '__main__':
    main()
