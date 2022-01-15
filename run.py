import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate

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

def start():
    """
    Start menu that the user can choose between 6 different tasks.
    """
    print("""
                --------MENU--------
                1. View sockets stock and price\n\
                2. View lights stock and price\n\
                3. View switches stock and price\n\
                4. Update stock\n\
                5. Get quote\n\
                6. Exit\n
                    """)
    while True:
        answer = input("Choose an option: \n")
        if answer == '1':
            print("Taking you to View sockets stock and price...\n")
            socket_type = SOCKETS.col_values(1)
            socket_stock = SOCKETS.col_values(5)
            print(f'{socket_type}:{socket_stock}')
            break
        elif answer == '2':
            print("Taking you to View lights stock and price......\n")
            lights_type = LIGHTS.col_values(1)
            lights_stock = LIGHTS.col_values(4)
            print(f'{lights_type}:{lights_stock}')
            break
        elif answer == '3':
            print("Taking you to View switches stock and price......\n")
            switches_type = SWITCHES.col_values(1)
            switches_stock = SWITCHES.col_values(4)
            print(f'{switches_type}:{switches_stock}')
            break
        elif answer == '4':
            print("Taking you to Update stock...\n")
           
            break
        elif answer == '5':
            print("Taking you to Get quote...\n")
            
            break
        elif answer == '6':
            print("Exiting...")
            exit_programme()
            break
        else:
            print("Not a valid input please enter a number 1-6")
            
start()

def exit_programme():
    """
    Shutting down program when user chose the exit task in menu
    """
    print("-------------------------------------------------------")
    print("---------------Thank you for using this----------------")
    print("------------------------APP!---------------------------")
    print("------------------------GOODBYE------------------------")
    print("-------------------------------------------------------")
