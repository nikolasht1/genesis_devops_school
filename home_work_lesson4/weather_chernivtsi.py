import requests
import math
import datetime


sity = "Chernivtsi"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q=Chernivtsi,ua&APPID=4f5c9c651c9780821d1f8fc42a8d12bf"

url = BASE_URL

response = requests.get(url).json()

today = datetime.date.today()
country = response['sys']['country']
temp = response['main']['temp']
temp = str(math.floor(temp -273.15))
humidity = str(response['main']['humidity'])
pressure = str(response['main']['pressure'])


print("Date today:   ",today)
print("My country:   ",country)
print("Sity:         ",sity)
print("Temperature:  ",temp+"° C")
print("Humidity:     ",humidity,"%")
print("Atm. pressure:",pressure,"kPa")