# https://gist.github.com/jsonbrazeal/745e118b37479b875a8d

import paho.mqtt.client as mqtt

def on_connect(mqttc, userdata, rc):
    print('connected...rc=' + str(rc))
    mqttc.publish(topic='device/sensor/temperature', payload='80', qos=0)

def on_disconnect(mqttc, userdata, rc):
    print('disconnected...rc=' + str(rc))

def on_message(mqttc, userdata, msg):
    print('message received...')
    print('topic: ' + msg.topic + ', qos: ' + str(msg.qos) + ', message: ' + str(msg.payload))

def on_publish(mqttc, userdata, mid):
    print('message published')
    mqttc.disconnect()

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_message = on_message
mqttc.on_publish = on_publish
mqttc.connect(host='localhost', port=1883)
mqttc.loop_forever()
