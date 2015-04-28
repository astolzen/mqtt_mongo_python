#!/bin/python

import paho.mqtt.publish as publish
import time

while True:
    publish.single("test/time", time.strftime("%c"), hostname="localhost")
    time.sleep(1)


