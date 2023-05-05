"""
Task 1
Robots.txt
Download and save to file robots.txt from wikipedia, twitter websites etc.
"""

print("\nTASK ONE\n")

import requests

url = "https://www.w3schools.com/python/python_file_write.asp"
resp = requests.get(url)
f = open("robots.txt", "w")
f.write(str(resp.content))
f.close()

"""
Task 2
Load data
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ . 
As a result, store all comments in chronological order in JSON and dump it to a file.
"""

print("\nTASK TWO\n")


base_url = "https://api.pushshift.io/reddit/comment/search/"


def get_data(url, params):
    r = requests.get(base_url, params=params)

    return r.json()


data = get_data(base_url, {"subreddit": "cars"})
data["data"].reverse()
# for comment in data["data"]:
#     print(comment["utc_datetime_str"])

f = open("subreddit.txt", "w")
f.write(str(data))
f.close()

"""
Task 3
The Weather app
Write a console application which takes as an input a city name and returns current weather in the format of 
your choice. For the current task, you can choose any weather API or website or use openweathermap.org 
"""

print("\nTASK THREE\n")

import json


def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "0d9c962624238b5dde144cb742d71bef"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    data = response.json()

    temp = round((data['main']['temp']) - 273.15, 2)
    desc = data['weather'][0]['description']
    wind_speed = data['wind']['speed']

    weather_data = f"Temperature: {temp} C\nDescription: {desc}\nWind speed: {wind_speed} m/s"

    return weather_data


def main():
    city = input("Enter a city name: ")
    weather_data = get_weather(city)
    print(f"\nCurrent weather in {city}:\n{weather_data}")


if __name__ == '__main__':
    main()



