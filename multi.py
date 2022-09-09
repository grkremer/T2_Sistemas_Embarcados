from concurrent.futures import process
from PIL import Image, ImageFilter
from multiprocessing import Pool
import glob
import os
import threading
import pyRAPL

import time

pyRAPL.setup() 


def processaImagem(name):
    image = Image.open(name)
    image = image.convert("L")
    image = image.filter(ImageFilter.FIND_EDGES)
    image.save("saida/"+name.replace("entrada/", ""))
    return




def limpa():
    files = glob.glob('saida/*')
    for f in files:
        os.remove(f)

@pyRAPL.measure
def processingFunction():
    names = glob.glob('entrada/*')
    print(names)
    if __name__ == '__main__':
        with Pool(16) as p:
            p.map(processaImagem, names)
    print("Done!")


def threadingFunction():
    names = glob.glob('entrada/*')
    print(names)
    threads = []
    for name in names:
        threads.append(threading.Thread(target=processaImagem,args=(name,)))
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print("Done!")
        

def single():
    names = glob.glob('entrada/*')
    print(names)
    for name in names:
        processaImagem(name)
    print("Done!")


def main():
    limpa()
    
    start = time.time()
    
    processingFunction()
    
    end = time.time()
    print(end - start)

    

main()