#!/usr/bin/env python3
import sys
import json
from datetime import datetime

for line in sys.stdin:
    try:
        fields = line.strip().split('\t')
        if len(fields) != 5:
            raise ValueError("Malformed")

        timestamp, user_id, action_type, content_id, metadata_str = fields
        datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        json.loads(metadata_str)

        print(f"{timestamp}\t{user_id}\t{action_type}\t{content_id}\t{metadata_str}")
    except Exception:
        # Could also use stderr for counters if supported
        continue
