import requests

# API key and URL
api_key = "3e24cc34e54c59132c14a74c"
base_url = "https://v6.exchangerate-api.com/v6/"

while True:
    # Get user input
    from_currency = input("What currency do you want to convert from? (e.g., EUR, USD): ").upper()
    to_currency = input("What currency do you want to convert to? (e.g., EUR, USD): ").upper()
    amount = input("What amount do you want to convert? ")

    # Ensure the amount is a valid number
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        continue

    # Construct the URL for the API request
    url = f"{base_url}{api_key}/latest/{from_currency}"

    # Make the API request
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

    # Ask the user if they want to continue converting or not
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
