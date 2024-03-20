# MQTT
MQTT stands for Message Queuing Telemetry Transport. It's a lightweight messaging protocol designed for constrained devices and low-bandwidth, high-latency, or unreliable networks. MQTT is commonly used for IoT (Internet of Things) applications where devices need to communicate with each other or with a central server.
### 1. Creating venv
After cloning the repository, you need to create virtual environment in your directory. Run the command `python3 -m venv mqtt_venv`. Activate the venv by command `source mqtt_venv/bin/activate`, now you are in venv.
### 2. Installing requirements
Install the required libraries running the command `pip install -r requirements.txt`
### 3. Installing broker
It communicates between MQTT clients, providing message routing, delivery, and management features. I chose mosquitto broker.
```bash
sudo apt update
sudo apt install mosquitto
sudo apt install mosquitto-clients
sudo systemctl start mosquitto
sudo systemctl enable mosquitto
```
### 4. Coding
I chose topic Chat/Python, and broker address `localhost` not to use online providers. It's initial port is `1883`
### 5. Running the code
Run the code on many terminals with `./client.py` enter your name and send messages to each other.
### 6. Following the process
If you want to see who's connected to broker and on which ip, run the command `sudo tail -f /var/log/mosquitto/mosquitto.log`.
And after the whole process is done, you can delete information about previous connection by command `sudo truncate -s 0 /var/log/mosquitto/mosquitto.log`.
