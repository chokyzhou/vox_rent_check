from concurrent.futures import thread
import threading
import subprocess
import time
import re
from os import listdir
from os.path import isfile, join
from bs4 import BeautifulSoup

def price_query():
    files = [f for f in listdir('./') if isfile(join('./', f))]
    file = open([f for f in files if re.search("html$",f)][0], "r")

    soup = BeautifulSoup(file, 'html.parser')

    t = soup.select("div[href='a1u'] > div > div > span > span")
    out = "".join(re.findall("[0-9]+", str(t[0])))
    
    file.close()
    
    return out

def crawl():
    while True:
        subprocess.run("scrapy crawl prices".split())
        time.sleep(3600)
    
def log_process():
    while True:
        price = price_query()
        print("Current price for 1b1b is " + price)
        time.sleep(10)

if __name__ == "__main__":
    threading.Thread(target=crawl).start()
    threading.Thread(target=log_process).start()
    