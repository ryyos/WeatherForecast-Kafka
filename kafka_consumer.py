import argparse
import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
from libs import Parser
from libs import Logs
from libs import Writer
from requests import Response
from icecream import ic

class Main:
    def __init__(self, server: str, topic_kc: str, topic_kp: str, path: str) -> None:
        self.__topic_kp = topic_kp
        self.__parser = Parser()
        self.__logs = Logs()
        self.__path = path
        self.__writer = Writer()
        self.__kafka_produser = KafkaProducer(bootstrap_servers=server)
        self.__kafka_consumer = KafkaConsumer(topic_kc, bootstrap_servers=server)


    def main(self):
        try:
            for message in self.__kafka_consumer:
                results: Response = self.__parser.fetch_data(location=message.value.decode("utf-8"))
                if results != 404:
                    self.__writer.ex(path=f'{self.__path}/{message.value.decode("utf-8")}.json', content=results.json())
                    self.__logs.info(requests=message.value.decode("utf-8"), status=results.status_code, offset=message.offset, response=results.json())
                    self.__kafka_produser.send(topic=self.__topic_kp, value=bytes(json.dumps(results.json()), 'utf-8'))
                    

        except KeyboardInterrupt:
            ic("stoped")



if __name__ == "__main__":
    request = argparse.ArgumentParser(description='Weatherstack scraping and distributed with kafka')
    request.add_argument('--server_k', '--sk', type=str, default='127.0.0.1:9092', help='Enter your Kafka server[defaulth: 127.0.0.1:9092]')
    request.add_argument('--topic_kc', '--kc', type=str, default='weather', help='Enter your Kafka topic')
    request.add_argument('--topic_kp', '--kp', type=str, default='elastic', help='Enter your Kafka topic')
    request.add_argument('--path', '--p', type=str, default='data', help='Enter the path if you want to save the scraping results locally')
    request = request.parse_args()

    main = Main(server=request.server_k , topic_kc=request.topic_kc, topic_kp=request.topic_kp, path=request.path)
    main.main()


