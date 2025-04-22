#!/usr/bin/env python3
import sys

for line in sys.stdin:
    try:
        _, user_id, action_type, _, _ = line.strip().split('\t')
        print(f"{user_id}\t{action_type}\t1")
    except:
        continue
