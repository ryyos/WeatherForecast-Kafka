import logging
from datetime import datetime as time

class Logs:
    def __init__(self) -> None:

        logging.basicConfig(datefmt='%m/%d/%Y %I:%M:%S %p', encoding="utf-8", level=logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        console = logging.StreamHandler()
        console.setLevel(level=logging.INFO) 
        console.setFormatter(formatter)

        file_log = logging.FileHandler(filename="logs/logging.log", encoding="utf-8")
        file_log.setLevel(level=logging.DEBUG)
        file_log.setFormatter(formatter)

        logger = logging.getLogger()
        for existing_handler in logger.handlers[:]:
            logger.removeHandler(existing_handler)

        logger.addHandler(console)
        logger.addHandler(file_log)

    def ex(self, status: int, offset: int, city: str) -> None:
        logger = logging.getLogger()
        logger.info(f"city: {city}")
        logger.info(f"offset: {offset}")
        logger.info(f"status: {status}")