import requests

def saatiedot(paikkakunta, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        saakuvaus = data['weather'][0]['description']
        lampotila = data['main']['temp']

        lampotila_celsius = lampotila - 273.15

        print(f"Sää {paikkakunta}: {saakuvaus}")
        print(f"Lämpötila: {lampotila_celsius:.2f} °C")

    else:
        print("Säätilojen hakeminen epäonnistui. ")

paikkakunta = input("Anna paikkakunnan nimi: ")
api_key = input("Anna api-avain: ")

saatiedot(paikkakunta, api_key)