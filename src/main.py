import requests

# API key and url
api_key = "bVpcjeNUDqsgsTxvAbkmA2QAFsJiHk"
url = "https://www.amdoren.com/api/currency.php"

while True:
    # Get user input
    first_conversion = input("What currency do you want to convert from? (e.g., EUR, USD): ").upper()
    second_conversion = input("What currency do you want to convert to? (e.g., EUR, USD): ").upper()
    amount = input("What amount do you want to convert? ")

    # The URL query parameters
    params = {
        "api_key": api_key,
        "from": first_conversion,
        "to": second_conversion,
        "amount": amount
    }

 # Make the API request
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    data['error'] == 0:
    converted_amount = data['amount']
    print(f"{amount} {first_conversion} is equal to {converted_amount} {second_conversion}.")

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
