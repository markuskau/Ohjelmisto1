import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        joke = data.get('value')
        print("Chuck Norris- joke:")
        print(joke)

    else:
        print("Chuck Norris- joke not found")

get_chuck_norris_joke()