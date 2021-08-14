import pyowm
owm = pyowm.OWM('604c5862add216fc85112ca19d69ce7f')

city ="Gaibandha,Gobindaganj"
location = owm.weather_manager().weather_at_place(city)

weather = location.weather

temp = weather.temperature(unit='celsius')
status = weather.detailed_status

cleaned_temp_data = (int(temp['temp']))
print('The temperature today in',city,'is',cleaned_temp_data,'Degrees celsius.')
print('The day today will have ',status, '.')