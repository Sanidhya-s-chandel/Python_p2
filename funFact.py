import random
import requests

def get_fun_fact():
    try:
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        if response.status_code == 200:
            return response.json().get("text", "Could not fetch a fun fact.")
        else:
            return "Could not fetch a fun fact. Try again later!"
    except requests.RequestException:
        return "Error connecting to the fun facts API. Check your internet connection."

if __name__ == "__main__":
    print("Did you know?")
    print(get_fun_fact())