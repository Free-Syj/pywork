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
    #print("downloading with urllib2", url, "-", filename)
    if( os.path.exists(filename) and os.path.getsize(filename)>4096 ):
        return
    try:
        f = urllib2.urlopen(url, timeout=8)
        with open(filename, "wb") as code:
            code.write(f.read())
    except urllib2.URLError as e:
        print("download", url, ":", e.reason)
    except Exception as ee:
        print('exception:', ee.args[0])

def process_task(i, queue, lock):
    print('Process to down %s:(%s)' % (i, os.getpid()))
    isRun = True
    while True:
        if( queue.empty() ):
            time.sleep(2)
        try:
            #lock.acquire()lock.release()
            tk = queue.get(True) #queue[0]
            #del queue[0]
        except Exception as e:
            print('queue get ex:', e)
        finally:
            pass
            #lock.release()
        print('pid:%s url:%s file:%s list:%d' % (os.getpid(), tk['url'], tk['filename'], queue.qsize()))
        # try:
        #     if tk['break']:
        #         print('break is:', tk['break'])
        #         break
        # except Exception as e:
        #     print("task", e.__traceback__)
        try:
            downloadByUrllib2(tk['url'], tk['filename'])
        except Exception as e:
            print('download ex:', e)
    print('pid:%s end.................' % (os.getpid()))

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
        if( segurl.find('/') == -1 ):
            basename,fname = os.path.split(m3u8url)
            filename = segurl
            segurl = basename + '/' + filename
        else:
            startpos = segurl.rindex('/')
            filename = segurl[startpos+1:]
        tk = {'url': segurl,
            'filename': filename}
        alltask.append(tk)

    pnum = multiprocessing.cpu_count()
    print('cpu_count:', pnum)
    print('alltask', len(alltask))
    manager = multiprocessing.Manager()
    mlist = manager.Queue()
    mlock = manager.Lock()
    procpool = multiprocessing.Pool(processes=pnum)
    for i in range(pnum):
        procpool.apply_async(process_task, args=(i, mlist, mlock))
    procpool.close()

    for j in alltask:
        #mlock.acquire()
        mlist.put(j)
        print('append list count:%d' % (mlist.qsize()))
        #mlock.release()
    for j in range(pnum):
        #mlock.acquire()
        mlist.put({'break': True})
        #mlock.release()
    print('Waiting for all subprocesses done...')
    procpool.join()
    print('All subprocesses done.')
    print("download done;")


