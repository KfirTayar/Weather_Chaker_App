import requests
from datetime import datetime
import streamlit as st
import matplotlib.pyplot as plt

def get_weather(city_name, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        weather_data = response.json()

        # Extract data safely
        city = weather_data.get("name", "Unknown City")
        temperature = weather_data["main"].get("temp", "N/A")
        humidity = weather_data["main"].get("humidity", "N/A")
        weather = weather_data["weather"][0].get("description", "No description available")

        return {
            "city": city,
            "temperature": temperature,
            "humidity": humidity,
            "weather": weather,
        }
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return None
    except KeyError as e:
        st.error(f"Missing data in API response: {e}")
        return None


# Streamlit app
st.title('Weather Checker App 🌦️')

# Input for the city name
city_name = st.text_input("Enter the name of the city:", "")

# Button to fetch weather details
if st.button("Check Weather"):
    if city_name.strip():
        api_key = st.secrets["OPENWEATHER_API_KEY"]
        if not api_key:
            st.error("API key not found! Add it to Streamlit secrets.")
        weather = get_weather(city_name, api_key)

        if weather:
            st.subheader(f"Weather Details for {weather['city']} 🌍")

            # Display metrics
            col1, col2 = st.columns(2)
            col1.metric("Temperature", f"{weather['temperature']}°C")
            col2.metric("Humidity", f"{weather['humidity']}%")
            st.text(f"Weather Condition: {weather['weather'].capitalize()}")

            # Plotting temperature and humidity
            labels = ['Temperature (°C)', 'Humidity (%)']
            values = [weather['temperature'], weather['humidity']]

            fig, ax = plt.subplots()
            bars = ax.bar(labels, values, color=['skyblue', 'orange'])
            ax.bar_label(bars, fmt='%.1f')
            ax.set_ylim(0, max(values) + 10)
            plt.title("Weather Data Overview")
            st.pyplot(fig)
        else:
            st.error("Could not fetch weather details. Please check the city name.")
    else:
        st.error("Please enter a city name!")


