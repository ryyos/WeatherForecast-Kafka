import argparse
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


    def main(self):
        try:
            for message in self.__kafka_consumer.accept():
                results: Response = self.__parser.fetch_data(location=message.value.decode("utf-8"))
                if results != 404:
                    self.__writer.ex(path=f'{self.__path}/{message.value.decode("utf-8")}.json', content=results.json())
                    self.__logs.info(requests=message.value.decode("utf-8"), status=results.status_code, offset=message.offset, response=results.json())
                    

        except KeyboardInterrupt:
            ic("stoped")



if __name__ == "__main__":
    request = argparse.ArgumentParser(description='Weatherstack scraping and distributed with kafka')
    request.add_argument('--server', '--s', type=str, default='127.0.0.1:9092', help='Enter your Kafka server[defaulth: 127.0.0.1:9092]')
    request.add_argument('--topic', '--t', type=str, default='weather', help='Enter your Kafka topic')
    request.add_argument('--path', '--p', type=str, default='data', help='Enter the path if you want to save the scraping results locally')
    request = request.parse_args()

    main = Main(server=request.server , topic=request.topic, path=request.path)
    main.main()


