import requests
import streamlit as st
import folium
import matplotlib.pyplot as plt
from streamlit_folium import folium_static

def fetch_weather(city_name, api_key):
    # API endpoint - Relies on information from this url
    url = "http://api.openweathermap.org/data/2.5/weather"

    # Parameters for the API request
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        # Make the API request
        response = requests.get(url, params=params)
        response.raise_for_status()
        weather_data = response.json()

        # Extract necessary data
        city = weather_data.get("name", "Unknown City")
        temperature = weather_data["main"].get("temp", "N/A")
        humidity = weather_data["main"].get("humidity", "N/A")
        weather = weather_data["weather"][0].get("description", "No description available")
        icon_code = weather_data["weather"][0].get("icon", "")
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"


        return {
            "city": city,
            "temperature": temperature,
            "humidity": humidity,
            "weather": weather,
            "icon_url": icon_url,
            "coord": weather_data["coord"]
        }

    # Raise an error if the request has not succeeded
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return None

    except KeyError as e:
        st.error(f"Missing data in API response: {e}")
        return None

def fetch_map(city_name, lat, lon):

    # Create a Folium map centered on the city coordinates
    f = folium.Figure(width='60%', height='500px')
    m = folium.Map(location=[lat, lon], zoom_start=10).add_to(f)
    folium.Marker([lat, lon], popup=f"Weather in {city_name}").add_to(f)

    # Display the map in Streamlit
    folium_static(f)


def create_weather_plot(labels, values):
    fig, ax = plt.subplots(figsize=(4, 6))
    bars = ax.bar(labels, values, color=['skyblue', 'orange'])
    ax.bar_label(bars, fmt='%.1f')
    ax.set_ylim(0, max(values) + 10)
    plt.title("Weather Data Overview")
    return fig