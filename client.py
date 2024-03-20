#!/usr/bin/python3
import paho.mqtt.client as mqtt
import time

broker_address = "localhost"
broker_port = 1883

# Callback functions for MQTT events
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")  
    else:
        print("Failed to connect to broker")

    client.subscribe("Chat/Python")

def on_message(client, userdata, msg):
    sender_name, message = msg.payload.decode().split(":", 1)
    if message.strip() == "left the chat":
        print(f"{sender_name.strip()} left the chat")
    else:
        print(f"{sender_name.strip()}: {message.strip()}")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, broker_port, 60)

client.loop_start()
time.sleep(0.2)

print("Type the message after you entered the name\nIf you want to left the chat, type exit")
username = input("Enter your name: ")

try:
    while True:
        message = input()
        if message.lower() == 'exit':
            client.publish("Chat/Python", f"{username}: left the chat")
            time.sleep(1)  # Ensure the message is sent before exiting
            break
        client.publish("Chat/Python", f"{username}: {message}")
        time.sleep(0.5)
except KeyboardInterrupt:
    pass 

