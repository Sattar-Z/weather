import requests
import json
import tkinter as tk



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


def get_weather_data(location):
    api_key = "YOUR_API_KEY"  # replace with your own API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data
    else:
        return None

def show_weather():
    location = location_entry.get()
    data = get_weather_data(location)
    if data:
        weather = data['weather'][0]['main']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather_label.config(text=f"Weather: {weather}")
        temperature_label.config(text=f"Temperature: {temperature}°C")
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_speed_label.config(text=f"Wind Speed: {wind_speed} km/h")
    else:
        weather_label.config(text="Error: Could not retrieve weather data")

get_weather_button = tk.Button(
    text="Get Weather",
    font=("Open Sans", 16),
    bg=fg_color,
    fg=bg_color,
    command=show_weather
)
get_weather_button.pack(pady=(20, 0))

root.mainloop()
