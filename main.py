import tkinter
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

import requests
from datetime import datetime
import json
import pytz
import pycountry_convert as pc


# Colors
co0 = "#2E2E2E"
co1 = "#FFFFFF"
co2 = "#A0C4FF"

morning_bg = "#E3F2FD"
afternoon_bg = "#FFE0B2"
night_bg = "#1E1E2F"
bg = morning_bg


# Window config
window = Tk()
window.title('')
window.geometry('320x350')
window.configure(bg=bg)
ttk.Separator(window, orient="horizontal").grid(row=0, columnspan=1, ipadx=157)


# Top frame
top_frame = Frame(window, width=320, height=50, bg=co1, pady=0, padx=0)
top_frame.grid(row=1, column=0)


# Body frame
body_frame = Frame(window, width=320, height=300, bg=bg, pady=0, padx=0)
body_frame.grid(row=2, column=0, sticky=NW)

style = ttk.Style(window)
style.theme_use('clam')

# Return info
def info():
    key = '7a41c9a9fa31295e2ab9dbacbd031a2d'
    city = location_entry.get()
    api_link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'

    # Request
    r = requests.get(api_link)

    # Convert data
    data = r.json()
    print(data)

    # Get zone, country and time
    country_code = data['sys']['country']
    zone = pytz.country_timezones[country_code]
    country = pytz.country_names[country_code]
    timezone = pytz.timezone(zone[0])
    local_time = datetime.now(timezone)
    local_time = local_time.strftime("%Y-%m-%d | %H:%M:%S %p")

    # Get weather
    temp_k = data['main']['temp']
    temp_c = temp_k - 273.15
    # print(f"{temp_c:.2f}")
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description']

    # Change info
    def country_to_continent(i):
        country_alpha = pc.country_name_to_country_alpha2(i)
        country_continen_code = pc.country_alpha2_to_continent_code(country_alpha)
        country_continent_name = pc.convert_continent_code_to_continent_name(country_continen_code)

        return country_continent_name

    continent = country_to_continent(country)

    # Push info to label
    city_label['text'] = city.title() + " - " + country + " / " + continent
    date_label['text'] = local_time
    temp_label['text'] = f"{temp_c:.0f}"
    degree_label['text'] = '°C'
    pressure_label['text'] = "Pressure: " + str(pressure) + " hPa"
    humidity_label['text'] = "Humidity: " + str(humidity) + "%"
    wind_label['text'] = "Wind Speed: " + str(wind_speed) + " m/s"
    description_label['text'] = description.title()

    # Theme logic
    zone_period = datetime.now(timezone)
    zone_period = zone_period.strftime("%H")

    zone_period = int(zone_period)

    if 0 <= zone_period <= 5:
        image = Image.open('images/night_moon.png')
        bg = night_bg

        city_label['fg'] = co1
        date_label['fg'] = co1
        temp_label['fg'] = co1
        degree_label['fg'] = co1
        pressure_label['fg'] = co1
        humidity_label['fg'] = co1
        wind_label['fg'] = co1
        description_label['fg'] = co1
    elif 6 <= zone_period <= 11:
        image = Image.open('images/morning_sun.png')
        bg = morning_bg

        city_label['fg'] = co0
        date_label['fg'] = co0
        temp_label['fg'] = co0
        degree_label['fg'] = co0
        pressure_label['fg'] = co0
        humidity_label['fg'] = co0
        wind_label['fg'] = co0
        description_label['fg'] = co0
    elif 12 <= zone_period <= 17:
        image = Image.open('images/afternoon_sun.png')
        bg = afternoon_bg

        city_label['fg'] = co0
        date_label['fg'] = co0
        temp_label['fg'] = co0
        degree_label['fg'] = co0
        pressure_label['fg'] = co0
        humidity_label['fg'] = co0
        wind_label['fg'] = co0
        description_label['fg'] = co0
    elif 18 <= zone_period <= 23:
        image = Image.open('images/night_moon.png')
        bg = night_bg

        city_label['fg'] = co1
        date_label['fg'] = co1
        temp_label['fg'] = co1
        degree_label['fg'] = co1
        pressure_label['fg'] = co1
        humidity_label['fg'] = co1
        wind_label['fg'] = co1
        description_label['fg'] = co1
    else:
        pass

    image = image.resize((130, 130))
    global imagem_tk
    imagem_tk = ImageTk.PhotoImage(image)

    icon_label = Label(body_frame, image=imagem_tk, bg=bg)
    icon_label.place(x=162, y=50)


    window.configure(bg=bg)
    top_frame.configure(bg=bg)
    body_frame.configure(bg=bg)
    
    city_label['bg'] = bg
    date_label['bg'] = bg
    temp_label['bg'] = bg
    degree_label['bg'] = bg
    pressure_label['bg'] = bg
    humidity_label['bg'] = bg
    wind_label['bg'] = bg
    description_label['bg'] = bg


# Top frame config
location_entry = Entry(top_frame, width=20, justify='left', font=("", 14), highlightthickness=1, relief='solid')
location_entry.place(x=15, y=10)

check_weather_btn = Button(top_frame, command=info, text='Check', bg=co1, fg=co2, font=("Ivy 9 bold"), relief='raised', overrelief='ridge')
check_weather_btn.place(x=250, y=10)


# Body frame config
city_label = Label(body_frame, text='', anchor='center', bg=bg, fg=co0, font=("Arial 14"))
city_label.place(x=10, y=4)

date_label = Label(body_frame, text='', anchor='center', bg=bg, fg=co0, font=("Arial 10"))
date_label.place(x=10, y=54)

temp_label = Label(body_frame, text='', anchor='center', bg=bg, fg=co0, font=("Arial 45"))
temp_label.place(x=10, y=100)

degree_label = Label(body_frame, text='', anchor='center', bg=bg, fg=co0, font=("Arial 10 bold"))
degree_label.place(x=85, y=110)

pressure_label = Label(body_frame, text='', anchor='center', bg=bg, fg=co0, font=("Arial 10"))
pressure_label.place(x=10, y=184)

wind_label = Label(body_frame, text='', anchor='center', bg=bg, fg=co0, font=("Arial 10"))
wind_label.place(x=10, y=212)

humidity_label = Label(body_frame, text='', anchor='center', bg=bg, fg=co0, font=("Arial 10"))
humidity_label.place(x=10, y=240)

description_label = Label(body_frame, text='', anchor='center', bg=bg, fg=co0, font=("Arial 10"))
description_label.place(x=170, y=190)

window.mainloop()