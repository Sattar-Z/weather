import tkinter as tk
import requests


bg_color = "#1F1F1F"
fg_color = "white"


root = tk.Tk()
root.title("Weather App")
root.configure(bg=bg_color)


logo_image = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(image=logo_image, bg=bg_color)
logo_label.pack(pady=(20, 0))


location_label = tk.Label(
    text="Location:",
    font=("Open Sans", 16),
    bg=bg_color,
    fg=fg_color
)
location_label.pack(pady=(20, 10))

location_entry = tk.Entry(font=("Open Sans", 16))
location_entry.pack()


temperature_label = tk.Label(
    text="",
    font=("Open Sans", 64, "bold"),
    bg=bg_color,
    fg=fg_color
)
temperature_label.pack(pady=(20, 0))


weather_label = tk.Label(
    text="",
    font=("Open Sans", 24),
    bg=bg_color,
    fg=fg_color
)
weather_label.pack()


def get_weather():
    location = location_entry.get()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid=<5b395d8f0e559f6a785eac58f1f22348>&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"].title()
        temperature_label.config(text=f"{temperature}°C")
        weather_label.config(text=weather)
    else:
        temperature_label.config(text="Error")
        weather_label.config(text="Could not retrieve weather data")


get_weather_button = tk.Button(
    text="Get Weather",
    font=("Open Sans", 16),
    bg=fg_color,
    fg=bg_color,
    command=get_weather
)
get_weather_button.pack(pady=(20, 0))


root.mainloop()
