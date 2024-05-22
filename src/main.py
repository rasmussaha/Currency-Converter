import requests

# API key and url
api_key = "30ebdcdf9cb24a9d851c26046e9bd25e"
url = "https://api.currencyfreaks.com/v2.0/convert/latest?from=usd&to=pkr&amount=500&apikey=YOUR_APIKEY"

while True:
    # Get user input
    from_currency = input("What currency do you want to convert from? (e.g., EUR, USD): ").upper()
    to_currency = input("What currency do you want to convert to? (e.g., EUR, USD): ").upper()
    amount = input("What amount do you want to convert? ")

    # The URL query parameters
    params = {
        "apikey": api_key,
        "from": from_currency,
        "to": to_currency,
        "amount": amount
    }

 # Make the API request
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    data['error'] == 0:
    converted_amount = data['amount']
    print(f"{amount} {from_currency is equal to {converted_amount} {to_currency}.")

    # Ask the user if they want to continue converting
    while True:
        stop = input("Do you want to continue converting? yes/no: ").strip().lower()
        if stop == "no":
            print("Stopping the conversion process.")
            break
        elif stop == "yes":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if stop == "no":
        break
