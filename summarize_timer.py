import os
from datetime import datetime, timedelta
# timedelta allows easier time calculations than pulling from the timestamp manually

def summarize():
    with open('timestamps.txt', 'r') as f:
        lines = f.readlines()
    
    start_time = None
    total_time = timedelta()
    interruptions = 0
    
    for line in lines:
        status, timestamp = line.strip().split(',')
        timestamp = datetime.fromisoformat(timestamp)
        
        if status == 'start':
            start_time = timestamp
        elif status == 'stop':
            if start_time is not None:
                interruptions += 1
                total_time += (timestamp - start_time)
    
    summary_text = f"{interruptions} interruptions. {total_time.seconds // 60} minutes {total_time.seconds % 60} seconds off task"
    
    with open('summaries.txt', 'a') as f:
        f.write(f"{datetime.now()}: {summary_text}\n")

    os.remove('timestamps.txt')
