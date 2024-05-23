# Currency Converter

The Currency Converter is a Python application that converts amounts between different currencies using real-time exchange rates from the ExchangeRate-API.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

Steps to install your project locally:

```bash
git clone https://github.com/rasmussaha/Currency-Converter.git
cd Currency-Converter
```

## Usage

```python
# Example of usage
import requests

# API key and base URL
api_key = "YOUR_API_KEY"
base_url = "https://v6.exchangerate-api.com/v6/"

while True:
    from_currency = input("What currency do you want to convert from? (e.g., EUR, USD): ").upper()
    to_currency = input("What currency do you want to convert to? (e.g., EUR, USD): ").upper()
    amount = input("What amount do you want to convert? ")

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        continue

    url = f"{base_url}{api_key}/latest/{from_currency}"

    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Could not retrieve data from the API.")
        continue

    data = response.json()

    if to_currency in data["conversion_rates"]:
        rate = data["conversion_rates"][to_currency]
        converted_amount = rate * amount
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
    else:
        print("Error: Could not retrieve conversion rate for the specified currencies.")

    stop = input("Do you want to continue converting? yes/no: ").strip().lower()
    if stop == "no":
        print("Stopping the conversion process.")
        break

```


## Features

- Real-time currency conversion
- Convert amounts to 150+ currencies

## Contributing

I am open to contributions! Please follow these steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Project Link: [https://github.com/rasmussaha/Currency-Converter](https://github.com/rasmussaha/Currency-Converter)

