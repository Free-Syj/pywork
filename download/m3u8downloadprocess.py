#!/usr/bin/python
# -*- coding: utf-8 -*-
import multiprocessing
import os, time, random
import sys
import m3u8
import socket
import urllib.request as urllib2

#socket.setdefaulttimeout(3)
# urllib2
def downloadByUrllib2(url, filename):
    print("downloading with urllib2", url, "-", filename)
    try:
        f = urllib2.urlopen(url, timeout=2)
        with open(filename, "wb") as code:
            code.write(f.read())
    except urllib2.URLError as e:
        print("download", url, ":", e.reason)

def process_task(i, tk ):
    print('Process to down %s:(%s)--%s:%s' % (i, os.getpid(), tk['url'], tk['filename']))
    print('url:%s file:%s'%(tk['url'], tk['filename']))
    downloadByUrllib2(tk['url'], tk['filename'])
    #while True:
    #    tk = queue.get(True)

# m3u8 parser
if __name__=='__main__':
    if(len(sys.argv)<2):
        print("please input m3u8 url")
        exit(-1)
    print("args:", len(sys.argv), "1:", sys.argv[1])
    m3u8url = sys.argv[1]
    stpos = m3u8url.rindex('/')
    fname = m3u8url[stpos + 1:]
    downloadByUrllib2(m3u8url, fname)
    m3u8obj = m3u8.load(fname)
    alltask = []
    for segment in m3u8obj.segments:
        segurl = segment.absolute_uri
        startpos = segurl.rindex('/')
        filename = segurl[startpos+1:]
        tk = {'url': segurl,
            'filename': filename}
        alltask.append(tk)
    taskq = multiprocessing.Queue()
    pnum = multiprocessing.cpu_count()
    print('cpu_count:', pnum)
    print('alltask',len(alltask))
    procpool = multiprocessing.Pool(processes=4)
    for i, pn in enumerate(alltask):
        procpool.apply_async(process_task, args=(i, pn,))
    procpool.close()
    print('Waiting for all subprocesses done...')
    procpool.join()
    print('All subprocesses done.')
    print("download done;")


