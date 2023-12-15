from kafka import KafkaConsumer

class Consumer:
    def __init__(self, server: str) -> None:
        self.__server = server
        self.__topic = "city"
        self.__consumer = KafkaConsumer(self.__topic, bootstrap_servers=[self.__server])
        pass

    def accept(self) -> str:
        return self.__consumer