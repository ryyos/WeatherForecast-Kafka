from libs import Parser
from libs import Consumer
from icecream import ic

class Main:
    def __init__(self, server: str) -> None:
        self.__kafka_consumer = Consumer(server=server)
        # self.__parser = Parser()


    def ex(self):
        try:
            while True:
                for message in self.__kafka_consumer.accept():
                    ic(message.value.decode("utf-8"))

        except KeyboardInterrupt:
            ic("stoped")


        # self.__parser.extract_data(city="jakarta")
        pass

if __name__ == "__main__":
    main = Main(server="127.0.0.1:9092")
    main.ex()


