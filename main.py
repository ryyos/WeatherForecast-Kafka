from libs import Parser
from libs import Consumer
from libs import Producer
from libs import Logs
from libs import Writer
from requests import Response
from icecream import ic

class Main:
    def __init__(self, server: str, topic: str, path: str) -> None:
        self.__parser = Parser()
        self.__logs = Logs()
        self.__path = path
        self.__writer = Writer()
        self.__kafka_consumer = Consumer(server=server, topic=topic)
        self.__kafka_produser = Producer(server=server)


    def ex(self):
        try:
            while True:
                for message in self.__kafka_consumer.accept():
                    results: Response = self.__parser.fetch_data(city=message.value.decode("utf-8"))

                    self.__writer.ex(path=f'{self.__path}/{message.value.decode("utf-8")}.json', content=results.json())

                    self.__logs.ex(city=message.value.decode("utf-8"), status=200, offset=message.offset)
                    

        except KeyboardInterrupt:
            ic("stoped")


if __name__ == "__main__":
    main = Main(server="127.0.0.1:9092", topic="city", path="data")
    main.ex()


