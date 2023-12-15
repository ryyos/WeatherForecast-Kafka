import requests
from icecream import ic
from libs.utils.writer import Writer


class Parser:
    def __init__(self) -> None:
        self.__api_key = '6927bf67fa11f657090746f42303cfff'
        pass

    def extract_data(self, city: str):
        response = requests.get(url=f"http://api.weatherstack.com/current?access_key=6927bf67fa11f657090746f42303cfff&query={city}")

        
