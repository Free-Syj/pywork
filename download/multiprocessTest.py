__author__ = 'shuyj'

from multiprocessing import Pool
from multiprocessing import Queue
import os, time, random
qq = Queue()

def long_time_master(name):
    print('Run master task %s (%s)...' % (name, os.getpid()))
    for i in range(10):
        qq.put(i)
def long_time_task(name, ch):
    print('Run task %s (%s)...%s' % (name, os.getpid(), ch))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    while True:
        print('get:',qq.get(True))
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())

    taskq = Queue()
    p = Pool(4)
    p.apply_async(long_time_master, args=(9,))
    ulist = ['htt','sssss','aaaa','ddddd']
    for i,ch in enumerate(ulist):
        p.apply_async(long_time_task, args=(i, ch,))
    print('Waiting for all subprocesses done...')

    p.close()
    for i in range(15,20):
        qq.put(i)
    p.join()
    print('All subprocesses done.')