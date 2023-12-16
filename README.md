<h1 align="center" >Hello 👋, I'm Ryo</h1>
<h3 align="center" >An independent backend developer</h3>

<h1 align="center" >Welcome To WeatherForecast-Kafka⛅</h1>

> This project is my practice playground for learning Apache Kafka

## Feature

- This program will provide the weather forecast for the next 6 days and update data every minute, hour and day
- supports searching for many locations, not only by city or province, but also by airport, restaurant and many more
- Using Apache Kafka for data distribution
- Easy connection with the Kafka server just by changing the available flags
- very detailed and detailed data for even every minute

## Tech

- [requests](https://docs.python-requests.org/) is an easy-to-use Python library for interacting with APIs and making HTTP requests
- [kafka-python](https://kafka-python.readthedocs.io/) is a Python library that provides functionality for interacting with Apache Kafka, a streaming data processing platform
- [fake_useragent](https://pypi.org/project/fake-useragent/) is a Python library that provides an easy way to generate fake user-agent strings for HTTP requests
- [icecream](https://github.com/gruns/icecream) is a Python library that provides a simple and informative way to log code, helping with monitoring program execution flows.

## Requirement

- [Python](https://www.python.org/) v3.11.6+
- [kafka-python](https://kafka-python.readthedocs.io/) v2.0.0+
- [icecream](https://github.com/gruns/icecream) v2.1.3+
- [fake_useragent](https://pypi.org/project/fake-useragent/) v1.4.0+
- [requests](https://docs.python-requests.org/) 2.31.0+

## Installation

> To run this program you need to install some libraries with the command

```sh
pip install kafka-python icecream fake_useragent
```

## Example Usage

```bash
# Clone this repositories
git clone https://github.com/ryosoraa/WeatherForecast-Kafka.git

# go into the directory
cd WeatherForecast-Kafka

```

### Start Main

```bash
python main.py --topic weater --server_k 127.0.0.1:9092 --path data
```

|    Flag    | Alias |                          Descriptions                           |          Example          |    Defaulth    |
| :--------: | :---: | :-------------------------------------------------------------: | :-----------------------: | :------------: |
|  --topic   |  -t   |                     Enter your Kafka topic                      |      --topic weater       |     weater     |
| --server_k |  -sk  |                     Enter your Kafka server                     | --server_k 127.0.0.1:9092 | 127.0.0.1:9092 |
|   --path   |  -p   | Enter the path if you want to save the scraping results locally |        --path data        |      data      |

## 🚀Structure

```
│   LICENSE
│   main.py
│   README.md
│
├───data
│       blitar.json
│       jakarta.json
│       surabaya.json
│       tanggerang.json
│
├───libs
│   │   __init__.py
│   │
│   ├───helpers
│   │   │   writer.py
│   │
│   ├───kafka
│   │   │   ConsumerRequest.py
│   │   │   ProduserResponse.py
│   │
│   ├───service
│   │   │   parser.py
│   │
│   ├───utils
│   │   │   log.py
│
└───logs
       logging.log
```

## Author

👤 **Rio Dwi Saputra**

- Twitter: [@ryosora12](https://twitter.com/ryosora12)
- Github: [@ryosoraa](https://github.com/ryosoraa)
- LinkedIn: [@rio-dwi-saputra-23560b287](https://www.linkedin.com/in/rio-dwi-saputra-23560b287/)

<a href="https://www.linkedin.com/in/ryosora/">
  <img align="left" alt="Ryo's LinkedIn" width="24px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
</a>
<a href="https://www.instagram.com/ryosoraaa/">
  <img align="left" alt="Ryo's Instagram" width="24px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" /> 
</a>
