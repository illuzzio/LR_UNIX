import time
import logging

print("Script started. Use: [Ctrl+C] to exit.")
while True:
    a = ("Hello world! Test service is alive!")
    b = (time.ctime())
    print("[%s] - %s" %(b,a))
    logging.basicConfig(filename='test.log', filemode="w", level=logging.INFO)
    logging.info("[%s] - %s" %(b,a))
    time.sleep(5)
