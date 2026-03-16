from header import logger, client, API_KEY_OF_OPENWEATHER, WeatherMonitor
from httpx import RequestError, HTTPStatusError
from datetime import datetime
#from header import API_KEY

def save_history(name_of_city, temteratura_of_city):
    time_search = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("history_search.txt","a", encoding="utf-8") as f:
        f.write(f"<<<[{time_search}]>>> City: {name_of_city}, Temp: {temteratura_of_city}\n")

# Function to get weather information
def get_weather(city_name=""):
    try:
        logger.info(f"Getting user information from {city_name}")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY_OF_OPENWEATHER}&units=metric"

        response = client.get(url)
        response.raise_for_status()

        data_from_server = response.json() 

        # The Response Schema appears at:
        # https://openweathermap.org/current?collection=current_forecast
        weather_data = WeatherMonitor(
            city=data_from_server["name"],
            temperature=data_from_server["main"]["temp"],
            description=data_from_server["weather"][0]["description"]
        )

        print("-" * 30)
        print(f"🌍 City: {weather_data.city}")
        print(f"🌡️ Temperature: {weather_data.temperature}°C")
        print(f"☁️ Description: {weather_data.description}")
        print("-" * 30)

    except RequestError as e:
        logger.error("Network error")
        print("Network error: Check your internet connection.")

    except HTTPStatusError as e:
        if e.response.status_code == 404: 
            logger.error(f"City not found: {city_name}")
            print(f"Error: City '{city_name}' not found. Please check the city name.")
        elif e.response.status_code == 401:
            logger.error("Unauthorized access.")
            print("Error: Unauthorized access - check your API key.")
        else:
            print(f"Server error: {e.response.status_code}")

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"There is an unexpected error.{e}")

    finally: 
        temp_of_city = weather_data.temperature if 'weather_data' in locals() else "Null"
        save_history(city_name, temp_of_city)
        
        logger.info("Request process finished.")
        print("Request process finished.\n")