
import threading
import time
from utils import fn_timer
from multiprocessing.dummy import Pool
import requests
from utils import urls
 
 # Aplicación: use un solo hilo para descargar el contenido de varias páginas web
@fn_timer
def download_using_single_thread(urls):
    resps = []
    for url in urls:
        resp = requests.get(url)
        resps.append(resp)


        
    return resps
 
 # Aplicación: use varios hilos para descargar el contenido de varias páginas web
@fn_timer
def download_using_multi_thread(urls):
    threads = []
    for url in urls:
        threads.append(threading.Thread(target = requests.get,args = (url,)))
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
 
 # Aplicación: use el grupo de subprocesos para descargar el contenido de varias páginas web
@fn_timer
def download_using_pool(urls):
    pool = Pool(20)
         # El primer parámetro es el nombre de la función, y el segundo parámetro es un objeto iterable, que es la lista de parámetros requerida por la función
    resps = pool.map(requests.get,urls)
    pool.close()
    pool.join()
    return resps
 
def main():
         # 1. Use un solo hilo
    resps = download_using_single_thread(urls)
    print (len(resps))
         # Salida:
    '''
    [finished function:download_using_single_thread in 6.18s]
    20
    '''
         # 2. Utilice subprocesos múltiples
    download_using_multi_thread(urls)
         # Salida:
    '''
    [finished function:download_using_multi_thread in 0.73s]
    20
    '''
 
         # 3. Usar grupo de subprocesos
    resps = download_using_pool(urls)
    print (len(resps))
         # Salida:
    '''
    [finished function:download_using_pool in 0.84s]
    20
    '''
 
if __name__ == '__main__':
    main()