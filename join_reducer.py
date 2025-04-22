#!/usr/bin/env python3
import sys

current_user = None
profile_info = None
activities = []

def emit():
    if profile_info:
        for action in activities:
            print(f"{current_user}\t{profile_info}\t{action}")

for line in sys.stdin:
    user_id, value = line.strip().split('\t', 1)

    if user_id != current_user and current_user:
        emit()
        profile_info = None
        activities = []

    current_user = user_id
    if value.startswith("P|"):
        profile_info = value[2:]
    elif value.startswith("A|"):
        activities.append(value[2:])

if current_user:
    emit()
