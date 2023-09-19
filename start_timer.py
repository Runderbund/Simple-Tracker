from datetime import datetime

def write_timestamp(status):
    with open('timestamps.txt', 'a') as f:
        f.write(f"{status},{datetime.now()}\n")

write_timestamp('start')
