# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 17:26:43 2020

@author: spal0
"""
import socket as s
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

broker = '192.168.1.224'
state_topic = 'home-assistant/pishake/Z'
#delay = 5

with open('/opt/settings/sys/ip.txt', 'r') as file:
    host = file.read().strip()

client = mqtt.Client("ha-client")
client.username_pw_set('user', 'password')
client.connect(broker)
client.loop_start()

port = 8888                             # Port to bind to
sock = s.socket(s.AF_INET, s.SOCK_DGRAM | s.SO_REUSEADDR)
sock.bind((host, port))
print ("Waiting for data on Port:", port)
while 1:                                # loop forever
    data, addr = sock.recvfrom(1024)    # wait to receive data
    data = data[1:len(data)]
    data.replace("{'EHZ', ")
    print (data)
    client.publish(state_topic, data)
