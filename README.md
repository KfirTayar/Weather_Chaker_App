# Weather Checker App

A Streamlit application that allows users to check the current weather for any city using the OpenWeather API. This app provides temperature, weather conditions, and humidity information based on user input.

## Features

- **City Input**: Users can input a city name to get its weather details.
- **Weather Information**: Displays current temperature, weather conditions, and humidity.
- **User-Friendly Interface**: Clean, interactive interface built with Streamlit.

## Requirements

- Python 3.7+
- Streamlit
- Requests
- OpenWeather API key

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
