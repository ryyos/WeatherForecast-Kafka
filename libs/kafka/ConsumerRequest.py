from kafka import KafkaConsumer

class Consumer:
    def __init__(self, server: str, topic: str) -> None:
        self.__consumer = KafkaConsumer(topic, bootstrap_servers=[server])
        

    def accept(self) -> str:
        return self.__consumer