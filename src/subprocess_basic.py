#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Create child processes and wait for them to complete execution
"""
import subprocess
import time

__author__ = "Magdalena Gawlinska"

start = time.time()

process_list = []
process_count = 5000
process_none = [None] * process_count

# create child processes that will do something (wait)
for idx in range(process_count):
    proc = subprocess.Popen(['sleep', '60'])
    process_list.append(proc)
    print(f"Process: {idx} created")

# wait for all processes to complete execution
while list(map(lambda x: x.poll(), process_list)) == process_none:
    print("I am waiting")

end = time.time()
delta = end - start

print(f" Execution time: {delta:.3}")
