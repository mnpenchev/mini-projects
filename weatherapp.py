# https://www.youtube.com/watch?v=D8-snVfekto   https://openweathermap.org/current
from tkinter import *
import requests

HEIGHT = 500
WIDTH = 600


def format_response(weather):
    try:
        name = weather['name']
        country = (weather['sys']['country'])
        desc = (weather['weather'][0]['description'])
        temp = (weather['main']['temp'])
        pressure = (weather['main']['pressure'])
        humidity = (weather['main']['humidity'])
        final_str = 'City: %s, %s \nConditions: %s \nTemperature (°C): %s \nPressure (hPa): %s \nHumidity: %s' % (name, country, desc, temp, pressure, humidity)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


def get_weather(city):
    weather_key = "8aa85aaa5057cb7d40c5eba10cc7daf8"
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)
    print(response.json())


# api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={your api key}
# 8aa85aaa5057cb7d40c5eba10cc7daf8


root = Tk()
root.title("Weather app")
root.iconbitmap('')

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = PhotoImage(file='landscape.png')
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = Frame(root, bd=5, bg='#80c1ff')  # bd - border
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = Entry(frame, bg='green', font=('Courier', 12))
entry.place(relwidth=0.65, relheight=1)

button = Button(frame, text="Get Weather", bg='grey', fg='red', font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = Frame(root, bd=10, bg='#80c1ff')
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame, font=('Courier', 20), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()

# pyinstaller.exe --onefile --icon=myicon.ico main.py
