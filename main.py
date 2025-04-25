from fastapi import FastAPI
from config import port
import uvicorn
from routers import weather

app = FastAPI()

app.include_router(weather.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=port)
