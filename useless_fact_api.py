#!/usr/bin/python3

import requests

print("10 seless fuckt:")
print()


for i in range(10):
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en", timeout=5)
    if response.status_code == 200:
        json_data = response.json()
        fuckt = json_data["text"]
        print(f"{i+1}. {fuckt}")
    else:
        print(f"Something wrong with fuckt {i+1}- doesn't work")
        