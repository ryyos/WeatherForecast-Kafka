from time import sleep
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=["127.0.0.1:9092"])

producer.send(topic="city", value=b"helloo")
sleep(3)

class Producer:
    def __init__(self, server: str) -> None:
        pass