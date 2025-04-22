#!/usr/bin/env python3
import sys

current_content = None
total = 0
THRESHOLD = 10  # Adjust based on histogram analysis

for line in sys.stdin:
    content_id, count = line.strip().split('\t')
    count = int(count)

    if current_content and current_content != content_id:
        if total >= THRESHOLD:
            print(f"{current_content}\tTrending\t{total}")
        total = 0

    current_content = content_id
    total += count

if current_content and total >= THRESHOLD:
    print(f"{current_content}\tTrending\t{total}")
