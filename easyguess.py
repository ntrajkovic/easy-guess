#!/usr/bin/env python3

# ********************************************************************
# easyguess.py
# Random number generator
# (C) 2022 Nenad Trajkovic, MIT License
# ********************************************************************

import time

def easy_guess():
    seed = int(time.time())
    a = 1664525    # Values from
    c = 1013904223 # Numerical Recipes
    m = 4294967296 # 2^32
    x0 = seed
    x1 = 1
    while True:
        x1 = (a * x0 + c) % m
        yield x1
        x0 = x1

if __name__ == "__main__":
    for i in easy_guess():
        print(i)
