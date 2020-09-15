from tkinter import *
import requests

def get_weather(city):
    weather_key = 'd1e5a0096dd76d51e54565ab57b44419'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID': weather_key, 'q': city, 'units':'metric'}
    response = requests.get(url, params = params)
    weather = response.json()

    lbl['text'] = format_response (weather)

def format_response(weather):
    print (weather)
    try:
        name = weather['name']
        condition =  weather['weather'][0]['description']
        temperature = int(weather['main']['temp'])
        return 'City: %s \n Condition: %s \nTemperature (°C): %s' % (name, condition, temperature)

    except:
        return 'Invalid Entry: Please try again'

window = Tk()
window.title("Welcome to City Information app")

window.geometry('600x500')

frame=Frame(window, bg='yellow', bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = Entry(frame, font=['Times', 20])
entry.place(relwidth=0.65, relheight=1)

btn = Button(frame, text="Go", font=['Times', 20], command=lambda: get_weather(entry.get()))
btn.place(relx=0.7, relwidth=0.3, relheight=1)

second_frame = Frame(window, bg='yellow', bd=10)
second_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

lbl = Label(second_frame, font=['Times', 20])
lbl.place(relwidth=1, relheight=1)

window.mainloop()