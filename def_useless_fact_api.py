#!/usr/bin/python3

"""
Generate random useless facts.

This module generates random useless facts using the uselessfacts.jsph.pl API.

"""

import requests

def generate_fuckt():
    number_of_fuckts = int(input("Please enter a number of facts:"))
    if number_of_fuckts > 128:
        print("Sorry memory, twój złom nie uciągnie tylu fucktów.")
        return

    for i in range(number_of_fuckts):
        response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en",
                            timeout=5)
        if response.status_code == 200:
            json_data = response.json()
            fuckt_id = json_data["id"]
            fuckt_text = json_data["text"]
            print(f"{i+1}) Id: {fuckt_id} Fact: {fuckt_text}")
        else:
            print(f"Something wrong with fuckt {i+1}- doesn't work")
            
generate_fuckt()
