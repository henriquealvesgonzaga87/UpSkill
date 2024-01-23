
import paho.mqtt.client as mqtt
import ssl
from datetime import datetime as dt
def on_connect(client, userdata, flags, reason_code, properties=None):
    client.subscribe(topic="Solar", qos=0)
def on_message(client, userdata, message, properties=None):
    print(
        f"{dt.now()} Received message {message.payload} on topic '{message.topic}' with QoS {message.qos}"
    )
def on_subscribe(client, userdata, mid, qos, properties=None):
    print(f"{dt.now()} Subscribed with QoS {qos}")
client = mqtt.Client(client_id="clientid", protocol=mqtt.MQTTv311, clean_session=True)
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.username_pw_set("verdados", "Ver_1234")
client.tls_set(ca_certs="isrgrootx1.pem")
client.connect(host="80d7deea43994008b36f90c46d8d3164.s1.eu.hivemq.cloud", port=8883, keepalive=60)

client.publish("Solar", payload="555", qos=0)

client.loop_forever()