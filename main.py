import tkinter
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk


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


# Top frame config
location_entry = Entry(top_frame, width=20, justify='left', font=("", 14), highlightthickness=1, relief='solid')
location_entry.place(x=15, y=10)

check_weather_btn = Button(top_frame, text='Check', bg=co1, fg=co2, font=("Ivy 9 bold"), relief='raised', overrelief='ridge')
check_weather_btn.place(x=250, y=10)


# Body frame config
city_label = Label(body_frame, text='Brasília - Brazil / South America', anchor='center', bg=bg, fg=co0, font=("Arial 14"))
city_label.place(x=10, y=4)

date_label = Label(body_frame, text='2025-07-21 | 10:50:00 AM', anchor='center', bg=bg, fg=co0, font=("Arial 10"))
date_label.place(x=10, y=54)

temp_label = Label(body_frame, text='27', anchor='center', bg=bg, fg=co0, font=("Arial 45"))
temp_label.place(x=10, y=100)

degree_label = Label(body_frame, text='°C', anchor='center', bg=bg, fg=co0, font=("Arial 10 bold"))
degree_label.place(x=85, y=110)

pressure_label = Label(body_frame, text='Pressure: 1013 hPa', anchor='center', bg=bg, fg=co0, font=("Arial 10"))
pressure_label.place(x=10, y=184)

wind_label = Label(body_frame, text='Wind Speed: 3.6 m/s', anchor='center', bg=bg, fg=co0, font=("Arial 10"))
wind_label.place(x=10, y=212)

humidity_label = Label(body_frame, text='Humidity: 84%', anchor='center', bg=bg, fg=co0, font=("Arial 10"))
humidity_label.place(x=10, y=240)

image = Image.open('images/morning_sun.png')
image = image.resize((130, 130))
image = ImageTk.PhotoImage(image)

icon_label = Label(body_frame, image=image, bg=bg)
icon_label.place(x=162, y=50)

description_label = Label(body_frame, text='Scattered Clouds', anchor='center', bg=bg, fg=co0, font=("Arial 10"))
description_label.place(x=170, y=190)






window.mainloop()