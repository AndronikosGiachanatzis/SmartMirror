import tkinter as tk
import aux
import requests
from APIError import *
import Weather


def create_window():
    # create window
    mainWindow = tk.Tk(className="Smart mirror")

    mainWindow.geometry("720x489")
    mainWindow['background'] = 'gray5'

    return mainWindow


def fetch_weather_data():
    # get parameters
    cityName = aux.cityName
    APIKey = aux.APIKey
    apiEndpoint = aux.weatherEndpoint

    # send request
    response = requests.get(apiEndpoint)

    # throw exception if respone code is different than 200
    if response.status_code != 200:
        raise APIError(f"GET {apiEndpoint} status={response.status_code}")

    # handle json response data
    jsonData = response.json()
    generalWeather = jsonData["weather"][0]
    weather = Weather.Weather(generalWeather["id"], generalWeather["main"], generalWeather["description"])
    print()
    

def main():
    name = "Andronikos"
    # create the main windows
    mainWindow = create_window()

    helloLabelFrame = tk.LabelFrame(mainWindow, bg=aux.backgroundColor, bd=1)
    helloLabel = tk.Label(
        master=helloLabelFrame,
        text=f"Hello {name}",
        fg="white",
        bg=aux.backgroundColor,
        font=(aux.defaultFont, 15)
    )


    helloLabel.pack()
    helloLabelFrame.pack(fill="both")

    print("Fetching weather data...")
    try:
        fetch_weather_data()
    except APIError as error:
        print(error)
    # show window
    mainWindow.mainloop()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

