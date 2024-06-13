import streamlit as st
import requests

st.title('IL METEO CHE VORREI...:rainbow::umbrella_with_rain_drops:	:mostly_sunny:	:lightning_cloud:')

from PIL import Image

image = Image.open('image.jpg')
st.image(image, caption='Hello World',width=800)



def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


API_key= 'b2c187b4c1cdb3bd61b2c6e56221b43d'
city_name=st.text_input('inserire ciccicittà:')
if city_name:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
    result=requests.get(url)
    json = result.json()

    temperatura = json['main']['temp']
    temperatura_conv = kelvin_to_celsius(temperatura)
    percepita = json['main']['feels_like']
    percepita_conv = kelvin_to_celsius(percepita)
    umidità = json['main']['humidity']
    

    if st.button('give it to me!'):
        st.success(f'la temperatura di {city_name} è {round(temperatura_conv, 2)} °C ')
        st.balloons()

    if st.button('push me!'):
        st.success(f'la temperatura percepita di {city_name} è {round(percepita_conv, 2)} °C ')
         
        

    if st.button('bottone'):
        st.success(f"l'umidità percepita a {city_name} è del {round(umidità, 2)} % ")




