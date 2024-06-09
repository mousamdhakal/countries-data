import json


def process_country_data(properties):
    with open('data.json', 'r') as file:
        countries_data = json.load(file)

    print("\n Countries data loaded from file data.json")

    # create a dictionary to store the countries data
    countries_dict = {}

    # loop through all countries:
    for country in countries_data:

        # Initialize an empty dictionary for the country info
        country_info = {}

        # Try to extract each property and add it to the country info
        for prop in properties:
            try:
                if prop in country:
                    if prop == "name":
                        country_info["common_name"] = country[prop]["common"]
                        country_info["official_name"] = country[prop]["official"]
                    else:
                        country_info[prop] = country[prop]
            except KeyError:
                print(f"Property {prop} not found for country {country['name']['common']}")

        # add the country info to the dictionary
        countries_dict[country["name"]["common"]] = country_info

    return countries_dict
