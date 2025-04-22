#!/usr/bin/env python3
import sys

for line in sys.stdin:
    try:
        _, _, action_type, content_id, _ = line.strip().split('\t')
        if action_type in ['like', 'share']:
            print(f"{content_id}\t1")
    except:
        continue
