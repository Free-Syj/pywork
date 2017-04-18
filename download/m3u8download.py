#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import m3u8
import socket
import urllib
import urllib.request as urllib2
import asyncio
socket.setdefaulttimeout(3)
# urllib
def downloadByUrllib(url, filename):
    print("downloading with urllib", url, "-", filename)
# python 2
#    try:
#        ures = urllib.urlopen(url)
#        with open(filename, "wb") as code:
#            code.write(ures.read())
#    except IOError as ex:
#        print("1download", url, "error:", ex)
#    urllib.urlretrieve(url, filename)

# urllib2
def downloadByUrllib2(url, filename):
    print("downloading with urllib2", url, "-", filename)
    try:
        f = urllib2.urlopen(url, timeout=2)
        with open(filename, "wb") as code:
            code.write(f.read())
    except urllib2.URLError as e:
        print("download", url, ":", e.reason)


async def wget(url):
    startpos = url.rindex('/')
    filename = url[startpos+1:]
    await downloadByUrllib2(url, filename)
    # print("wget with urllib2", url, "-", filename)
    # try: # not support @asyncio.coroutine
    #     f = await urllib2.urlopen(url, timeout=2)
    #     with await open(filename, "wb") as code:
    #         await code.write(f.read())
    # except urllib2.URLError as e:
    #     if isinstance(e.reason , socket.timeout):
    #         print("download", url, ":timeout")

# m3u8 parser
if(len(sys.argv)<2):
    print("please input m3u8 url")
    exit(-1)
print("args:", len(sys.argv), "1:", sys.argv[1])

m3u8url = sys.argv[1]
stpos = m3u8url.rindex('/')
fname = m3u8url[stpos + 1:]
downloadByUrllib2(m3u8url, fname)
m3u8obj = m3u8.load(fname)
loop = asyncio.get_event_loop()

tasks = [wget(segment.absolute_uri) for segment in m3u8obj.segments]
#for segment in m3u8obj.segments:
#    segurl = segment.absolute_uri
#    startpos = segurl.rindex('/')
#    filename = segurl[startpos+1:]
    #downloadByUrllib2(segurl, filename)
loop.run_until_complete(asyncio.wait(tasks))
print("download done;")
loop.close()


