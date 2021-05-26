import time
import os
  
while True:
    os.system("curl http://localhost:6800/schedule.json -d project=default -d spider=hot")
    time.sleep(3600)  #每隔一天运行一次 24*60*60=86400s