from data_processor import fetch_data, process_data

def main():
    # fields to fetch from the API, only selected fields will be fetched and processed for faster processing
    fields = ["name", "altSpellings", "capital", "population", "area", "language",
              "codes", "region"]
    countries_data = fetch_data.fetch_countries_data(fields)

    # if countries data is fetched successfully, process the data
    if countries_data:
        countries_dict = process_data.process_country_data()
        print("\nCountries data processed successfully.")

        # print the countries data in a readable format
        for country, info in countries_dict.items():

            # check if the info of the country is a dictionary
            if isinstance(info, dict):
                print(f"\nCountry: {country}")

                # Loop through each key value in the processed data
                for key, value in info.items():
                    print(f"{key}: {value}")
            else:
                print(f"\nCountry: {country}")
                print(f" Error: {info} \n");

    else:
        print("\nError processing countries data.")

if __name__ == "__main__":
    main()

