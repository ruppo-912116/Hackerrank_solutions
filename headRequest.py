import requests
import queue
from threading import Thread
import sys

concurrent = 200

def doWork():
    while True:
        url = q.get()
        url,status = getStatus(url) 
        resultShow(url,status)
        q.task_done()

#calling each urls from the text file and returning individual urls and their respective responses
def getStatus(url):
    x = requests.get(url)
    return url,x

#displaying each urls and their respective responses
def resultShow(url,status):
    print("url: "+url+"                status: " +status.text+"\n")

q = queue.Queue(concurrent * 2)

for i in range(concurrent):
     t = Thread(target = doWork)
     t.daemon = True
     t.start()
       
try:
    for url in open('urllist.txt'):
        q.put(url.strip())
    q.join() #block the main thread until all the workers have processed everything in the queue
except KeyboardInterrupt:
    sys.exit(1)
