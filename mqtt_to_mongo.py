#!/bin/python
# Subscribes to given Topics on MQTT and Posts Messages to Mongo
# Requires:
# -  paho.mqtt.client
# -  python-pymongo

import time
import sys
import paho.mqtt.client as mqtt
from pymongo import MongoClient

mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['test']
mongo_collection = mongo_db['testcol01']

mqtt_client_id = "mqtt-to-mongo"
mqtt_server = "localhost"
mqtt_topic = "#"

def on_connect(mqttc, obj, rc):
    print("Connected with rc: "+str(rc))

def on_message(mqttc, obj, msg):
     print("Topic: "+msg.topic+" Message: "+str(msg.payload))
     mongo_post= {"date": time.strftime("%c"),
                 "topic": msg.topic,
                 "message": str(msg.payload)}
     mongo_post_id = mongo_collection.insert(mongo_post)
     print "Posted to Mongo as ID: "+str(mongo_post_id)

def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)

mqttc = mqtt.Client(mqtt_client_id)

mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

mqttc.connect(mqtt_server, 1883, 60)
mqttc.subscribe(mqtt_topic, 0)

mqttc.loop_forever()

