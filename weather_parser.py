import requests
import json
from config import key, version
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass
class Hours:
    datetime: str
    temp: float
    humidity: float
    pressure: float


@dataclass
class Days:
    datetime: str
    tempmax: float
    tempmin: float
    temp: float
    humidity: float
    pressure: float
    hours: dict
    hours_class: dict = field(default_factory=dict)

    def __post_init__(self):
        for i in range(0, len(self.hours)):
            json_obj = json.loads(json.dumps(self.hours[i]))
            hour = Hours(**json_obj)
            self.hours_class[i] = hour


@dataclass
class WeatherRaw:
    queryCost: int
    latitude: float
    longitude: float
    resolvedAddress: str
    address: str
    timezone: str
    tzoffset: float
    days: dict
    days_class: dict = field(default_factory=dict)

    def __post_init__(self):
        for i in range(0, len(self.days)):
            json_obj = json.loads(json.dumps(self.days[i]))
            day = Days(**json_obj)
            self.days_class[i] = day


@dataclass
class Data:
    city: str
    date_from: str
    date_to: str
    temperature_c: dict
    humidity: dict
    pressure_mb: dict


@dataclass_json
@dataclass
class Service:
    service: str
    data: Data


def get_weather_raw(
    city: str,
    date_from: str,
    date_to: str,
    include="hours",
    elements="datetime,hours,tempmax,tempmin,temp,humidity,pressure",
) -> WeatherRaw:
    endpoint = (
        "https://weather.visualcrossing.com/"
        "VisualCrossingWebServices/rest/services/timeline/"
    )
    query_params = {
        "key": key,
        "location": city,
        "datestart": date_from,
        "dateend": date_to,
        "unitGroup": "metric",
        "include": include,
        "elements": elements,
    }
    response = requests.get(endpoint, query_params).json()
    weather_raw = WeatherRaw(**response)
    return weather_raw


def get_median(data):
    data.sort()
    number = int(len(data) / 2)
    return (data[number] + data[number - 1]) / 2


def get_average(data):
    average = 0
    for number in data:
        average = average + number

    return average / len(data)


def get_weather(date_from, date_to, city):
    """Функция вывода информации о погоде"""

    response = get_weather_raw(city, date_from, date_to)

    date_from = response.days_class[0].datetime
    date_to = response.days_class[len(response.days_class) - 1].datetime

    temp = []

    for date in response.days_class:
        for hour in response.days_class[date].hours_class:
            temp.append(response.days_class[date].hours_class[hour].temp)

    temp_out = {
        "average": get_average(temp),
        "median": get_median(temp),
        "min": min(temp),
        "max": max(temp),
    }

    weather = {"temperature_c": temp_out}
    return weather


def get_info():  # функция вывода общей информации о проекте
    return {"version": version, "service": "weather", "author": "p.zemlyanskiy"}
