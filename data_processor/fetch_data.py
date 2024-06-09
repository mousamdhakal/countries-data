import json
import requests


def fetch_countries_data(fields):
    baseUrl = "https://restcountries.com/v3.1/all"

    # loop through fields array and add to the url
    fields_str = ",".join(fields)
    url = f"{baseUrl}?fields={fields_str}"

    print(f"\n Please wait. Loading countries data ....")

    # fetch the data from the API
    response = requests.get(url)

    # check if the response is successful
    if response.status_code != 200:
        print(f"Error fetching data. Status code: {response.status_code}")
        return None
    else:
        countries_data = response.json()

        # save the country data in the file data.json
        with open('data.json', 'w') as file:
            json.dump(countries_data, file, indent=4)
        print("\nCountries data saved in file: data.json")
        return countries_data
