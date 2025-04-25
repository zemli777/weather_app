from datetime import datetime, timedelta
from fastapi import APIRouter
from pydantic import BaseModel
from weather_parser import get_weather, get_info
from schemas.weather import WeatherRequest
from dataclasses import field

router = APIRouter()


class ResponceModel(BaseModel):
    service: str
    data: dict = field(default_factory=dict)


@router.get("/info")
def get_info_hendler():
    info = get_info()
    return info


@router.get("/info/weather")
def get_weather_hendler(
    city: str = "SaintPeterburg",
    date_from: str = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d"),
    date_to: str = datetime.now().strftime("%Y-%m-%d"),
):
    request_data = WeatherRequest.model_validate(
        {"city": city, "date_from": date_from, "date_to": date_to}
    )
    weather = get_weather(
        request_data.date_from, request_data.date_to, request_data.city
    )
    return {"service": "weather", "data": weather}
