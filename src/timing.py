#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Collection of timing-related functions
"""
import subprocess
import time

__author__ = "Magdalena Gawlinska"

from timeit import repeat


def time_your_sort(algorithm, data, repeat_count):
    setup_code = f"from __main__ import {algorithm}"
    stmt = f"{algorithm}({data})"
    executions = repeat(stmt=stmt, setup=setup_code, repeat=repeat_count, number=1)

    print(f"Algorithm: {algorithm}: Execution times: {executions}. "
          f"Minimum execution time: {min(executions)}")