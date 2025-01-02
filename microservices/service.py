import json
import time
from fluent import sender, event
import os

FD_HOST = os.getenv('FD_HOST', 'localhost')
sender.setup('service',host=FD_HOST, port=5000) # change service1 to MS_HOST

for i in range(20):
    print("sent message")
    event.Event('info_log', {"message":"This is a test log"})
    time.sleep(5)

