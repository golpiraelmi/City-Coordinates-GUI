from tkinter import *
import requests

#  Get the data: 'USGS Earthquakes > 4.5 in the past 24 hours'
#Website: https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php

url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson'
response = requests.get(url)
earthquakes = response.json()

def latest_earthquakes(input_number):
    num = len(earthquakes['features'])
    if input_number> num:
        print('There are ' + str(num) + ' earthquakes in the past month')
        input_number = num

    mag_l,lon_l, lat_l, loc_l=[],[],[],[]
    for i in range(input_number):
        time = earthquakes['features'][i]['properties']['time']
        mag = float(round(earthquakes['features'][i]['properties']['mag'],1))
        lon = earthquakes['features'][i]['geometry']['coordinates'][0]
        lat = earthquakes['features'][i]['geometry']['coordinates'][1]
        loc = earthquakes['features'][i]['properties']['place']
        mag_l.append(mag)
        lon_l.append(lon)
        lat_l.append(lat)
        loc_l.append(loc)

    for i in range(len(loc_l)):
       exec('Label%d=Label(second_frame, text="Magnitude: %s")\nLabel%d.pack()' % (i, mag_l[i], i))
       exec('Label%d=Label(third_frame, text="Coordinates: %f, %f")\nLabel%d.pack()' % (i, lat_l[i], lon_l[i], i))
       exec('Label%d=Label(forth_frame, text="%s,")\nLabel%d.pack()' % (i, loc_l[i], i))

# APP APPEARANCE---------------------------------------------------------------
window = Tk()
window.title("Earthquakes Greater Than 4.5 Richter in the Past 24h Hours")

window.geometry('900x800')

label=Label(window, text='Please enter the number of most recent earthquakes you wish to see:', font=['Times', 15])
label.place(relx=0.13, rely=0.02)

first_frame=Frame(window)
first_frame.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.1, anchor='n')

entry = Entry(first_frame, font=['Times', 20])
entry.place(relwidth=0.5, relheight=0.5)

btn = Button(first_frame, text="Recent Earthquakes", font=['Times', 20], command=lambda: latest_earthquakes(int(entry.get())))
btn.place(relx=0.5, relwidth=0.5, relheight=0.5)

second_frame = Frame(window)
second_frame.place(relx=0.1, rely=0.15, relwidth=0.45, relheight=0.85, anchor='n')

third_frame = Frame(window)
third_frame.place(relx=0.42, rely=0.15, relwidth=0.50, relheight=0.85, anchor='n')

forth_frame = Frame(window)
forth_frame.place(relx=0.80, rely=0.15, relwidth=0.45, relheight=0.85, anchor='n')

window.mainloop()