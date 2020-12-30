#
#
# IOTRFID Subscribe Module
#
# Receives inventory message from IOTRFID
# SwitchDoc Labs December 2020
#

import json
import paho.mqtt.client as mqtt

def filter_non_printable(str):

  return ''.join([c for c in str if ord(c) > 31 or ord(c) == 9])

#  The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):

    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and

    # reconnect then subscriptions will be renewed.

    client.subscribe("IOTRFID/#")

# he callback for when a PUBLISH message is received from the server.

def on_message(client, userdata, msg):
   print(msg.topic+" "+str(msg.payload.decode()))

   result = json.loads(msg.payload.decode())  # result is now a dict / filter start and stop characters
   print(result)
   InventoryRFID = result['d']['RFID_ID']



   print()
   print("IOTRFID Inventory Number Received From ID#"+result['d']['IOTRFID'])
   print("Inventory Item = " + InventoryRFID)
   print

# main program

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message


client.connect("localhost", 1883, 60)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.


client.loop_forever()




