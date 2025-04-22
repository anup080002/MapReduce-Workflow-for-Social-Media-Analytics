#!/usr/bin/env python3
import sys

for line in sys.stdin:
    parts = line.strip().split(',')
    if len(parts) >= 3:
        user_id = parts[0]
        profile = ','.join(parts[1:])
        print(f"{user_id}\tP|{profile}")
