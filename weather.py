import requests
import streamlit as st
import base64

api_key = "a6f81aff8e354cf14db2c448cbb27e5c"

def weather(city):
    """Fetch weather data from OpenWeatherMap API."""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()


def set_background(image_file):
    """Set a background image using base64 encoding."""
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def main():
    st.title("Weather App")

    set_background("weather.png") 
    
    city = st.text_input("Enter city name")

    if city:
        if st.button("submit"):
            data = weather(city)

            if data.get("cod") == 200:
                st.subheader(f"Weather in {data['name']}, {data['sys']['country']}")
                st.write(f"Temperature: {data['main']['temp']}°C")
                st.write(f"Humidity: {data['main']['humidity']}%")
                st.write(f"Weather: {data['weather'][0]['description'].capitalize()}")
                st.write(f"Wind Speed: {data['wind']['speed']} m/s")
            else:
                st.error("City not found. Please check the name and try again.")

if __name__ == "__main__":
    main()
 

