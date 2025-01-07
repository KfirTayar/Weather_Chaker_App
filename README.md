# Weather Checker App

A web application that allows users to check the current weather for any city using the OpenWeather API. The app provides temperature, weather conditions, humidity information, and a map of the city based on user input.

## Features

- **City Input**: Users can input a city name to get its weather details.
- **Weather Information**: Displays current temperature, weather conditions, and humidity.
- **City Map**: Shows the map of the city for better context.
- **User-Friendly Interface**: Clean and interactive design for an enhanced user experience.

## Dependencies

This project requires the following dependencies:

- **Python**: `^3.11`
- **Requests**: `^2.32.3`
- **Datetime**: `^5.5`
- **Streamlit**: `^1.41.1`
- **Matplotlib**: `^3.10.0`
- **Poetry Plugin Export**: `^1.8.0`
- **Folium**: `^0.19.4`
- **Streamlit-Folium**: `^0.24.0`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-checker-app.git

2. Navigate into the project folder:
    ```bash
    cd weather-checker-app
   
3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Set up your API key:

- Sign up for an OpenWeather account here to get your API key.
- Add your API key in the .streamlit/secrets.toml file:
   
 ```toml
 OPENWEATHER_API_KEY = "your_api_key_here"

## Usage
    
1. Run the app:
    ```bash
    streamlit run Program.py

2. Open the app in your browser at http://localhost:8501.

3. Enter the name of any city to get its weather details.
