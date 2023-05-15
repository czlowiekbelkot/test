#!/usr/bin/python3

"""
Generate 10 random useless facts.

This module generates 10 random useless facts using the uselessfacts.jsph.pl API.

"""

import requests

print("10 useless fuckt:")
print()

for i in range(10):
    response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en",
                            timeout=5)
    if response.status_code == 200:
        json_data = response.json()
        fuckt_id = json_data["id"]
        fuckt_text = json_data["text"]
        print(f"Id: {fuckt_id} Fact: {fuckt_text}")
    else:
        print(f"Something wrong with fuckt {i+1}- doesn't work")
