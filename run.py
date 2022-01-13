import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("price-calculator")


SOCKETS = SHEET.worksheet("sockets")
LIGHTS = SHEET.worksheet("lights")
SWITCHES = SHEET.worksheet("switches")
SALES = SHEET.worksheet("sales")

sockets_data = SOCKETS.get_all_values()
lights_data = LIGHTS.get_all_values()
switches_data = SWITCHES.get_all_values()
sales_data = SALES.get_all_values()

enter_input = ("Please select from the options above:")
answer = ""


def get_sales_data():
    """
    Get sales figures input from the user.
    """
    print("Please enter up to date sales figures.")
    print("Data should be 3 numbers, separated by commas.")
    print("Example: 10,20,30\n")
    print(input("Please insert sales values:"))

#get_sales_data()

#def update_sales():
    """ Function to update sales sheet within google spreadsheet
    """
    get_sales_data()
    print("Updating worksheet...\n")
    sales_worksheet = SHEET.worksheet(sales)
    sales_worksheet.append_row(data)
    print("Sales worksheet updated successfully!")

    #update_sales()

def main_menu():

    while True:
        sockets_data
        lights_data
        switches_data
        print("""---MENU---
        1.View Stock and Price
        2.Add Sales Data
        3.Add Stock Delivery
        4.Do Stock Take
        """)
        answer = input(enter_input)
        if answer == "1":
            print(sockets_data,lights_data,switches_data)
            break
        elif answer == "2":
           update_sales()
        elif answer == "3":
            stock_data = ([item[2:] for item in sockets_data] + [[item[2:] for item in lights_data]])
            input_data = []
            input_data = print("Please input what stock has been delivered")
            print(f'{stock_data} - {input_data}')
            break

main_menu()

