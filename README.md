# Countries of the World

Provides brief information about countries of the world. The information includes the country's name, capital, region,
population, and area.
This can be manipulated to include more information about the countries.

## Installation

1. Clone the repository

```bash
git clone https://github.com/mousamdhakal/countries-data.git
```

2. Make sure you have Python installed on your system. If not, download and install Python
   from [here](https://www.python.org/downloads/).

3. Run the script

```bash
python main.py
```

4. You can modify the fields in the `main.py` file to include more information about the countries.

## Modules

The modules defined in the script are:

1. fetch_data - Fetches the data from the restcountries API. It is responsible for fetching data from the Rest Countries
   API. It takes a list of fields as an argument, constructs a URL with these fields, and sends a GET request to the
   API.After receiving the response in JSON format, it :
   - Converts the JSON response to a Python dictionary.
   - Saves the data to a JSON file.
   - Returns the data.    
   

2. process_data - This module transforms the raw data from the API to structured and usable format for further use.
 It ensures only the fields that are specified in the properties  parameter are included in the final data. 
