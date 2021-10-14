#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 23:08:36 2021

@author: user
"""

from threading import Thread
import os
import math
import time

def calc():
    for i in range(0,4000000):
        math.sqrt(i)
        
threads = []

tstart = time.time()

for i in range(os.cpu_count()):
    print('registering thread %d' % i)
    threads.append(Thread(target=calc))
    
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
    
print("Total threadding time:", time.time() - tstart)