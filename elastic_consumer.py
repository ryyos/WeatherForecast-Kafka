import uuid
import json
from elasticsearch import Elasticsearch
from icecream import ic
from libs import Logs
from kafka import KafkaConsumer

class Elastic:
    def __init__(self, topic: str, server_k: str) -> None:
        self.__elasticsearch = Elasticsearch(['http://192.168.20.90:9200'])
        self.__logs = Logs()
        self.__kafka_consumer = KafkaConsumer(topic, bootstrap_servers= server_k)
        

    def send(self, index: str):

        try:
            for message in self.__kafka_consumer:
                response = self.__elasticsearch.index(index=index, body=json.loads(message.value), ignore=[400,404])
                ic(response)

        except KeyboardInterrupt:
            ic('Stopped')

if __name__ == '__main__':
    es = Elastic(topic='elastic', server_k='127.0.0.1:9092')
    es.send(index='weather_tomorrow')

