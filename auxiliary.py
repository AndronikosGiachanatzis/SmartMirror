'''
Define constants and auxiliary methods
'''

# background color for windows and frames
backgroundColor = "gray5"
defaultFont = "Helvetica"

APIKey = "API-KEY-HERE" # temporary, must hide it

# weather
cityName = "Thessaloniki"
weatherEndpoint = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={APIKey}"
