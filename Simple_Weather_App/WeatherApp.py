import requests as rq #a library to easily handle HTTP calls
import os
from dotenv import load_dotenv 
import GUI

# Load environment variables from .env
load_dotenv()


API_KEY = os.getenv("API_KEY") #the API key i got from weatherapi.com
BASE_URL = "http://api.weatherapi.com/v1/current.json" 

def fetch_data(city):
    response = rq.get(f"{BASE_URL}?key={API_KEY}&q={city}") #q = query , ? indicates the start of the query string
    data = response.json() #converts the APIs response to a python dictionary
    
    if "error" in data: #testing if the webserver contains the needed information for the given city
        return("the entered city does not exist, please try again")
    else: #fetching the data from the dictionary
        time = data["location"]["localtime"]
        temp_c = data["current"]["temp_c"]
        temp_f = data["current"]["temp_f"]
        weather = data["current"]["condition"]["text"]
        last_up = data["current"]["last_updated"]
        return (f"🌡 The temperature in {city} is {temp_c}°C / {temp_f} °F.\n "
                 f"☁ There are {weather} conditions.\n "
                 f"🕒 The localtime is: {time}.\n "
                 f"🔄 The data was last updated : {last_up}")
        
def get_input():
    city = GUI.entry.get()
    result = fetch_data(city)
    GUI.label.config(text=result)

