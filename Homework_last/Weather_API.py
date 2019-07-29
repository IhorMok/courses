# import pyowm
#
# owm = pyowm.OWM('dbb5aa8109f36495f0cf246fa483afe2', language = "ru")
#
#
# place = input("Enter your city: ")
# observation = owm.weather_at_place(place)
# w = observation.get_weather()
# print(w)




# ================
# 1. определять язык
# 2. возможно было вызвать из консоли
# import requests
# import _json
# def weather(city, lang):
#   key = 'dbb5aa8109f36495f0cf246fa483afe2'
#   param = {'q': city,'APPID': key, 'lang': lang}
#   r = requests.get('http://api.openweathermap.org/data/2.5/weather?&units=metric', params= param)
#   data = r.json()
#   return data
#
# def ask_city():
#   return input("Enter any city: ")
#
# def print_weather(data):
#   print("conditions:", data['weather'][0]['description'])
#   print("temp:", data['main']['temp'])
#   print("temp_min:", data['main']['temp_min'])
#   print("temp_max:", data['main']['temp_max'])
#   print("wind:", data['wind']['speed'], data['wind']['deg'])
#   print("pressure:", data['main']['pressure'])
#
# def define_language(city):
#   # city[0] in a-zA-Z
#   return 'en'
#
# city = ask_city()
# lang = define_language(city)
# weather_result = weather(city, lang)
# print_weather(weather_result)
# ================
#
import requests
import argparse
import _json

# python weather.py киев
# python weather.py kyiv
#
# 1. определять язык
# 2. возможно было вызвать из консоли

def weather(city, lang):
  key = 'dbb5aa8109f36495f0cf246fa483afe2'
  param = {'q': city, 'APPID': key, 'lang': lang}
  r = requests.get('http://api.openweathermap.org/data/2.5/weather?&units=metric', params=param)
  data = r.json()
  return data



def ask_city():
  return input("Enter any city: ")


def print_weather(data):
  print("conditions:", data['weather'][0]['description'])
  print("temp:", data['main']['temp'])
  print("temp_min:", data['main']['temp_min'])
  print("temp_max:", data['main']['temp_max'])
  print("wind:", data['wind']['speed'], "м/с" ',', data['wind']['deg'])
  print("pressure:", data['main']['pressure'])
  return

# def define_language(city):
#   # city[0] in a-zA-Z
#   return



if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Fetching a weather in the indicated city')
  parser.add_argument('-lang', '--city', help='Indicate city')

  args = parser.parse_args()
  city = args.city
  # lang = define_language(city)
  weather_result = weather(city,lang)
  print_weather(weather_result)

# -lang en  --city Chernivtsi


#=============================================================
# import requests
# import json
# import argparse
#
# # python weather.py киев
# # python weather.py kyiv
#
# # 1. определять язык
# # 2. возможно было вызвать из консоли
#
# def weather(city, lang):
#   key = 'dbb5aa8109f36495f0cf246fa483afe2'
#   param = {'q': city,'APPID': key, 'lang': lang}
#   r = requests.get('http://api.openweathermap.org/data/2.5/weather?&units=metric', params= param)
#   data = r.json()
#   return data
#
# def ask_city():
#   return input("Enter any city: ")
#
# def print_weather(data):
#   print("conditions:", data['weather'][0]['description'])
#   print("temp:", data['main']['temp'])
#   print("temp_min:", data['main']['temp_min'])
#   print("temp_max:", data['main']['temp_max'])
#   print("wind:", data['wind']['speed'], data['wind']['deg'])
#   print("pressure:", data['main']['pressure'])
#
# def define_language(city):
#   # city[0] in a-zA-Z
#   return 'en'
#
# def main():
#   city = ask_city()
#   lang = define_language(city)
#   weather_result = weather(city, lang)
#   print_weather(weather_result)
#
# if __name__ == '__main__':
#   parser = argparse.ArgumentParser(description='Fetching a weather in the indicated city')
#   parser.add_argument('--city',
#                     help='Indicate city')
#
#   args = parser.parse_args()
#   print(args)
#   main()
#=================================================