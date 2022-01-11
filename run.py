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
SOCKETS = SHEET.worksheet('sockets')
LIGHTS = SHEET.worksheet('lights')
SWITCHES = SHEET.worksheet('switches')



def view_stock():
    """
    A function that prints out the current stock of materials with prices
    """

    print("Please select an option from the menu")

    stock_str = input('Enter your choice here:')
    sockets_stock = stock_str.split(',')
   
    def main():
        """
        Start menu that the user can choose between 4 different tasks.
        """
    print("""   --------MENU--------
                1.View Stock List w/Prices\n\
                2.Add Sales Data\n\
                3.Add Stock Delivery\n\
                4.Do Stock Take\n\
                    """)

    def view_stock():
      """
    Function to get all values from google sheet
    and show them as a list for each type.
     """

    view_stocks = SOCKETS.get_all_values()
    if view_stock:
        for socket in view_stocks:
            printing_all_values(socket)
    else:
        print("Stock is empty!")
    back_to_menu()

view_stock()    

def printing_all_values(sockets):
    """
    Function that takes all the existing values from worksheet
    and make it a loop with the materials type and prices
    """
    one_value = []
    for type, price in sockets.items():
        print(f'{type}: {price}')
    print("-----------------------------------")
    return one_value


