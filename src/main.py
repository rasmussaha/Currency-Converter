import urwid
import requests

# API key and URL
api_key = "3e24cc34e54c59132c14a74c"
base_url = "https://v6.exchangerate-api.com/v6/"

# Placeholder data for currencies
common_currencies = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD"]

class CurrencyConverterApp:
    def __init__(self):
        self.main_loop = None
        self.from_currency = None
        self.to_currency = None
        self.amount = None

        self.main_widget = urwid.Pile([
            urwid.Text("Select the currency to convert from or type your own:"),
            self.create_currency_buttons("from"),
            urwid.Edit(caption="Type your own 'from' currency: ", wrap='clip', align='center'),
            urwid.Text("Select the currency to convert to or type your own:"),
            self.create_currency_buttons("to"),
            urwid.Edit(caption="Type your own 'to' currency: ", wrap='clip', align='center'),
            urwid.Text("Enter the amount to convert:"),
            urwid.Edit(caption="", edit_text="", wrap='clip', align='center'),
            urwid.Button("Convert", on_press=self.convert)
        ])

    def create_currency_buttons(self, currency_type):
        buttons = []
        for currency in common_currencies:
            button = urwid.Button(currency)
            urwid.connect_signal(button, 'click', self.select_currency, (currency, currency_type))
            buttons.append(urwid.AttrMap(button, None, focus_map='reversed'))

        return urwid.GridFlow(buttons, cell_width=8, h_sep=2, v_sep=1, align='center')

    def select_currency(self, button, data):
        currency, currency_type = data
        if currency_type == "from":
            self.from_currency = currency
        elif currency_type == "to":
            self.to_currency = currency
        self.update_info()

    def update_info(self):
        self.main_widget.contents[0] = (urwid.Text(f"From: {self.from_currency} To: {self.to_currency} Amount: {self.amount or ''}"), self.main_widget.options())

    def convert(self, button):
        from_currency_edit = self.main_widget.contents[2][0]
        to_currency_edit = self.main_widget.contents[5][0]
        amount_edit = self.main_widget.contents[7][0]

        # Check if user entered custom currencies
        if from_currency_edit.edit_text.strip():
            self.from_currency = from_currency_edit.edit_text.strip().upper()
        if to_currency_edit.edit_text.strip():
            self.to_currency = to_currency_edit.edit_text.strip().upper()

        self.amount = amount_edit.edit_text

        if not self.from_currency or not self.to_currency or not self.amount:
            result = "Please select or enter currencies and enter an amount."
        else:
            try:
                amount = float(self.amount)
                url = f"{base_url}{api_key}/latest/{self.from_currency}"
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    rate = data["conversion_rates"].get(self.to_currency)
                    if rate:
                        converted_amount = rate * amount
                        result = f"{amount} {self.from_currency} is equal to {converted_amount:.2f} {self.to_currency}."
                    else:
                        result = "Conversion rate not available."
                else:
                    result = "Error fetching conversion rate."
            except ValueError:
                result = "Invalid amount. Please enter a numeric value."

        self.main_widget.contents.append((urwid.Text(result), self.main_widget.options()))
        self.main_loop.draw_screen()

    def run(self):
        self.main_loop = urwid.MainLoop(urwid.Filler(self.main_widget, valign='top'), unhandled_input=self.unhandled_keypress)
        self.main_loop.run()

    def unhandled_keypress(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

if __name__ == "__main__":
    app = CurrencyConverterApp()
    app.run()
