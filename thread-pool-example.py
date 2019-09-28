import urllib2 
from multiprocessing.dummy import Pool as ThreadPool 
from multiprocessing import cpu_count
import time

urls = [
  'http://www.python.org', 
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
]


def open_url_links():
	start_time = time.time()
	thread_no = cpu_count()
	print ("no of cpu cores: " , thread_no)

	# make the Pool of workers
	pool = ThreadPool(thread_no) 

	# open the urls in their own threads
	# and return the results
	results = pool.map(urllib2.urlopen, urls)

	# close the pool and wait for the work to finish 
	pool.close() 
	pool.join() 

	print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
	open_url_links()

