import requests
import json
import tkinter as tk

def get_weather_data(location):
    api_key = "63be7538793c875c44d785e0f3a18e98"  # replace with your own API key
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

# Create a GUI window
window = tk.Tk()
window.title("Weather App")

# Create GUI elements
location_label = tk.Label(window, text="Enter location:")
location_entry = tk.Entry(window, width=30)
get_weather_button = tk.Button(window, text="Get Weather", command=show_weather)
weather_label = tk.Label(window, text="")
temperature_label = tk.Label(window, text="")
humidity_label = tk.Label(window, text="")
wind_speed_label = tk.Label(window, text="")

# Add GUI elements to the window
location_label.grid(row=0, column=0, padx=10, pady=10)
location_entry.grid(row=0, column=1, padx=10, pady=10)
get_weather_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
weather_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
temperature_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
humidity_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
wind_speed_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI window
window.mainloop()
