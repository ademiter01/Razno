#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 23:11:09 2021

@author: user
"""

from multiprocessing import Process
import os
import math
import time

def calc():
    for i in range(0,4000000):
        math.sqrt(i)
        
processes = []

tstart = time.time()
for i in range(os.cpu_count()):
    print('registering process %d' % i)
    processes.append(Process(target=calc))
    
for process in processes:
    process.start()

for process in processes:
    process.join()
    
print("Total processing time:", time.time() - tstart)