#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import signal
import subprocess
import commands

import time

isRun = True

def signal_term(s, e):
    global isRun
    isRun = False
    print "recv TermSignal"

if __name__ == "__main__":
    #print sys.argv[0]
    global isRun
    signal.signal(signal.SIGINT, signal_term)
    signal.signal(signal.SIGQUIT, signal_term)
    signal.signal(signal.SIGTERM, signal_term)
    commandstr1 = "ffplay -autoexit -framedrop rtmp://pull.kitty.live.8686c.com/live/"
    commandstr2 = "ffplay -autoexit -framedrop rtmp://europepull.kitty.live.8686c.com/live/"
    commandstr3 = "ffplay -autoexit -framedrop rtmp://americapull.kitty.live.8686c.com/live/"
    commandstr = ""
    for i in range(1, len(sys.argv)):
        print "arg ", i, sys.argv[i]
        if sys.argv[i] == 1:
            commandstr = commandstr1
        elif sys.argv[i] == 2:
            commandstr = commandstr2
        elif sys.argv[i] == 3:
            commandstr = commandstr3
        else:
            commandstr = commandstr1
            commandstr += sys.argv[i];
            break;
        commandstr += sys.argv[i+1];
        # {
        #     1:lambda x: x+=" ",
        # }[sys.argv[i]]()
        # result = {
        #     'a': lambda x: x * 5,
        #     'b': lambda x: x + 7,
        #     'c': lambda x: x - 2
        # }[value](x)
    #subprocess调用方式
    #subprocess.call (["cmd", "arg1", "arg2"],shell=True)
    #p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #
    #for line in p.stdout.readlines():
	 #    print line,
    # retval = p.wait()

    # commands 调用方式
    # commands.getoutput("date")

    # os两种方式
    # tmp = os.popen('ls *.py').readlines()
    print "command:",commandstr
    while isRun:
        os.system(commandstr)
        time.sleep(1)
        # os.wait()

