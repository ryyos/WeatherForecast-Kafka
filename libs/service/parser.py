import requests
from icecream import ic
from libs.helpers.writer import Writer
from fake_useragent import FakeUserAgent

class Parser:
    def __init__(self) -> None:
        self.__writer = Writer()
        self.__user_agent = FakeUserAgent()

        self.__api_key = 'UZ8GOpIh0q5umvfA6Xkm6d3t3NUBlUSn'
        self.__proxies = {
            "http": "154.6.96.156:3128"
        }
        self.__headers = {
            "accept": "application/json",
            "User-Agent": self.__user_agent.random
        }
        

    def extract_data(self, city: str):
        response = requests.get(url=f"https://api.tomorrow.io/v4/weather/forecast?location={city}&apikey={self.__api_key}", proxies=self.__proxies)
        self.__writer.ex(path="private/percobaan.json", content=response.json())


        
