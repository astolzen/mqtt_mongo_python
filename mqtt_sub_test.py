#!/bin/python
#Simple Subscription Skript. Subscribes all Topics and Prints out all messages

import time
import sys
import paho.mqtt.client as mqtt

def on_connect(mqttc, obj, rc):
    print("rc: "+str(rc))

def on_message(mqttc, obj, msg):
#    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
     print "Topic: |"+msg.topic+"|"
     print "Message: |"+str(msg.payload)+"|"
     print "Time: |"+time.strftime("%c")+"|"
     print "---"

def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)

mqttc = mqtt.Client("pymqtt_to_mongo")

mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

mqttc.connect("localhost", 1883, 60)
mqttc.subscribe("#", 0)

mqttc.loop_forever()


