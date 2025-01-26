import tkinter as tk

def convert_currency():
    # Retrieve amount, base currency, and target currency from user inputs
    amount = float(entry.get())
    base_currency = base_currency_var.get()
    target_currency = target_currency_var.get()

    # Make a request to the exchange rate API to get the latest rates
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{base_currency}")
    data = response.json()  # Parse the response as JSON

    # Extract the conversion rate for the target currency from the API response
    conversion_rate = data['rates'][target_currency]

    # Calculate the converted amount
    converted_amount = amount * conversion_rate

    # Display the converted amount in the result_label
    result_label.config(text=str(converted_amount))

# Create the main window
window = tk.Tk()
window.title("Currency Converter")

# Label and Entry for entering the amount
label1 = tk.Label(window, text="Amount:")
label1.pack()

entry = tk.Entry(window)
entry.pack()

# Label and Dropdown for selecting the base currency
label2 = tk.Label(window, text="Base Currency:")
label2.pack()

base_currency_var = tk.StringVar(window)
base_currency_var.set("USD")  # Default base currency

# Provide options for base currency selection
base_currency_dropdown = tk.OptionMenu(window, base_currency_var, "USD", "EUR", "GBP", "INR")
base_currency_dropdown.pack()

# Label and Dropdown for selecting the target currency
label3 = tk.Label(window, text="Target Currency:")
label3.pack()

target_currency_var = tk.StringVar(window)
target_currency_var.set("EUR")  # Default target currency

# Provide options for target currency selection
target_currency_dropdown = tk.OptionMenu(window, target_currency_var, "USD", "EUR", "GBP", "INR")
target_currency_dropdown.pack()

# Label for displaying the converted amount
label4 = tk.Label(window, text="Converted Amount:")
label4.pack()

# Label to display the result of the currency conversion
result_label = tk.Label(window, text="")
result_label.pack()

# Button to trigger the currency conversion
button = tk.Button(window, text="Convert", command=convert_currency)
button.pack()

# Start the main event loop
window.mainloop()
