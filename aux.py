'''
Define constants and auxiliary methods
'''

# background color for windows and frames
backgroundColor = "gray5"
defaultFont = "Helvetica"

APIKey = "624d4871b5fd8859c8ba05ce88a58fe8" # temporary, must hide it

# weather
cityName = "Thessaloniki"
weatherEndpoint = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={APIKey}"