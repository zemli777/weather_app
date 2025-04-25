from pydantic import BaseModel, Field


class WeatherRequest(BaseModel):
    city: str = Field(..., min_length=3, max_length=30)
    date_from: str
    date_to: str
