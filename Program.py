import streamlit as st
from weather_functions import fetch_weather, fetch_map, create_weather_plot

# App title
st.title('Weather Checker App 🌦️')

# Input for the city name
city_name = st.text_input("Enter the name of the city:", "")

# Button to fetch weather details
if st.button("Check Weather"):
    if city_name.strip():

        # Fetch the API key from Streamlit secrets
        api_key = st.secrets.get("OPENWEATHER_API_KEY")

        if not api_key:
            st.error("API key not found! Add it to Streamlit secrets.")
        else:
            # Fetch weather details
            weather_data = fetch_weather(city_name, api_key)

            if weather_data:
                # Display city and weather details
                st.subheader(f"Weather Details for {weather_data['city']} 🌍")

                col1, col2, col3 = st.columns(3)

                with col1:
                    # Display weather icon
                    st.image(
                        weather_data['icon_url'],
                        width=80,
                        caption=f"{weather_data['weather'].capitalize()}"
                    )

                with col2:
                    st.metric("Temperature", f"{weather_data['temperature']} °C")

                with col3:
                    st.metric("Humidity", f"{weather_data['humidity']}%")

                # Creating temperature and humidity plot
                labels = ['Temperature (°C)', 'Humidity (%)']
                values = [weather_data['temperature'], weather_data['humidity']]
                fig = create_weather_plot(labels, values)

                col1, col2 = st.columns(2)

                with col1:
                    # Display plot
                    col1.pyplot(fig)

                with col2:
                    # Display map
                    fetch_map(city_name, weather_data["coord"]["lat"], weather_data["coord"]["lon"])

            else:
                st.error("Could not fetch weather details. Please check the city name.")

    else:
        st.error("Please enter a city name!")