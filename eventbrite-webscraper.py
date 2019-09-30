import requests
from bs4 import BeautifulSoup
import os
import sys
import collections
import time
from multiprocessing.dummy import Pool as ThreadPool 
from multiprocessing import cpu_count
from multiprocessing import Lock as Mutex

path_curr = os.getcwd()
url = 'https://www.eventbrite.com/d/netherlands/all-events/'
max_pages = 10
page = 1
trash_price_str = ['$', 'R', 'US']
# for each page
linkFile = open("links_with_threads.txt", "w")
weblist = set()
mutex = Mutex()
thread_no = cpu_count()
pool = ThreadPool(thread_no) 

def main(url, max_pages):
    for page in range(max_pages):
        main_page(page)
    for link in weblist:
        linkFile.write(link + "\n")
    linkFile.close()

def main_page(page):
    print(page)
    # create weblinks, eventlists as LIST
    # weblinks = 
    getEventLinks(url, page)
    #linkFile.write(str(page) + "\n")
    
    
def parseHref(link):
	mutex.acquire()
	aclass = link.findAll('a')
	href = aclass[0].get('href')
	weblist.add(href)
	mutex.release()
    		
def getEventLinks(url, page):
    
    eventlist = []
    
    full_url = url + '?page='+ str(page+1)
    source_code = requests.get(full_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
     
    urlContainer = soup.findAll('div', {'class': "eds-media-card-content__content__principal"})   

    '''
    for link in urlContainer:
        parseHref(link)
    '''
    pool.map(parseHref, urlContainer)
    
    
    
    '''
    for link in range(len(urlContainer)):
        aclass = urlContainer[link].findAll('a')
        href = aclass[0].get('href')
        weblist.add(href)        
     
    return weblist
    '''   

if __name__ == "__main__":
    start_time = time.time()
    main(url, max_pages)
    #pool.join()

    print("--- %s seconds ---" % (time.time() - start_time))
