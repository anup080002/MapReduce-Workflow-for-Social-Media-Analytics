#!/usr/bin/env python3
import sys

for line in sys.stdin:
    try:
        user_id, action, count = line.strip().split('\t')
        print(f"{user_id}\tA|{action}|{count}")
    except:
        continue
