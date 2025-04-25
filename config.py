import os
from dotenv import load_dotenv


load_dotenv()
key = os.getenv("API_KEY")
if len(key) != 25:
    raise ValueError("invalid API_KEY. Key len need to be 25")
port = int(os.getenv("PORT", default=8080))
version = os.getenv("VERSION", default="0.1.0")
