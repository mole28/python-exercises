import logging
import httpx
import os
from pydantic import BaseModel
from dotenv import load_dotenv


# Loads environment variables from the .env file.
# retrieves the OpenWeather API key using the os module.
load_dotenv()
API_KEY_OF_OPENWEATHER  = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY_OF_OPENWEATHER:
    raise ValueError("\n" + "!!"*15 +
        "Error: API Key not found!!!" +
        "Please create a .env file and add: OPENWEATHER_API_KEY=your_key" +
        "\nGoodbye")

#class WeatherMonitor(BaseModel):
class WeatherMonitor(BaseModel):
        city: str
        temperature: float
        description: str

# Set up logging
logger = logging.getLogger("my_log")
logger.setLevel(logging.INFO)
Formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.FileHandler('my_log.log')
handler.setFormatter(Formatter)
logger.addHandler(handler)

# Create an HTTP client
client = httpx.Client()