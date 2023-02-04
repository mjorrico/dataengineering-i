#!/usr/bin/env python3

import fileinput
import string
import re

last_word = None
count = 0

for line in fileinput.input():
    w, c = line.strip().split()
    c = int(c)

    if w == last_word:
        count += c
    else:
        if last_word: print(f"{last_word} {count}")
        last_word = w
        count = 1

print(f"{last_word} {count}")
