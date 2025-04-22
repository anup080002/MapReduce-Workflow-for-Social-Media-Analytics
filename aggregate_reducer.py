#!/usr/bin/env python3
import sys
from collections import defaultdict

current_user = None
action_counts = defaultdict(int)

def emit(user_id, counts):
    for action, count in sorted(counts.items(), key=lambda x: -x[1] if x[0] == "post" else 0):
        print(f"{user_id}\t{action}\t{count}")

for line in sys.stdin:
    try:
        user_id, action_type, count = line.strip().split('\t')
        count = int(count)
        if current_user != user_id and current_user is not None:
            emit(current_user, action_counts)
            action_counts = defaultdict(int)

        current_user = user_id
        action_counts[action_type] += count
    except:
        continue

if current_user:
    emit(current_user, action_counts)
