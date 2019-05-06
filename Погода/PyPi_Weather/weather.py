import pyowm
city = input('Введите город: ')
owm = pyowm.OWM('9365dc786b5320acb3761b07fafa9c90', language='ru')

observation = owm.weather_at_place(city)
w = observation.get_weather()
time = observation.get_reception_time(timeformat='iso')
temp = w.get_temperature('celsius')
cloudy = w.get_clouds()
wind_speed = w.get_wind()['speed']
vlajnost = w.get_humidity()
voshod = w.get_sunrise_time('iso')
zakat = w.get_sunset_time('iso') 


print("В городе" + str(city) + " сейчас температура - " + str(temp['temp']) + " °C ")
print("Время - " + str(time))
print("Скорость ветра - " + str(wind_speed) + " м/c")
print("Облачность - " + str(cloudy) + " %")
print("Влажность - " + str(vlajnost) + " %")
print("Восход солнца - " + str(voshod))
print("Закатсолнца - " + str(zakat))
