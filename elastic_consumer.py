import argparse
import json
from elasticsearch import Elasticsearch
from icecream import ic
from libs import Logs
from kafka import KafkaConsumer

class Elastic:
    def __init__(self, topic: str, server_k: str, server_el: str) -> None:
        self.__elasticsearch = Elasticsearch([server_el])
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
    request = argparse.ArgumentParser()
    request.add_argument('--topic', '--t', type=str, default='elastic')
    request.add_argument('--server_k', '--sk', type=str, default='127.0.0.1:9092')
    request.add_argument('--server_el', '--sel', type=str, default='http://192.168.20.90:9200')
    request.add_argument('--index', '--i', type=str, default='weather_tomorrow')
    request = request.parse_args()

    es = Elastic(topic=request.topic , server_k=request.server_k, server_el=request.server_el)
    es.send(index=request.index)

