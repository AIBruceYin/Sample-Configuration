import os
import time
import logging as log
import sys

log.basicConfig(format="[ %(levelname)s ] %(message)s", level=log.INFO, stream=sys.stdout)
log.info("Demo log output in container")
log.info("--Hello Container--")

log.info("Demo creating file in mount point")
f = open('./data.txt', 'a+')
f.write('Hello Python' + os.linesep)

log.info("Demo keep the container live with max limitation")
while True:
  time.sleep(5)
  log.info("--Enter terminal to do what you want --")
log.info("exit")
