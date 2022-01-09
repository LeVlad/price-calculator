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

sockets = SHEET.worksheet("sockets")

data = sockets.get_all_values()

sockets_value = 0
lights_value = 0
switches_value = 0

def get_values():
    """
    Get the values from the user
    """

    
print("Welcome to Materials Calculator\n")
print("""    -------1. Sockets --------\n
     -------2. Lights -------\n
    -------3. Switches -------\n""")

answer = ""
answer = input("Please select one of the options above:")
while True:
    if answer == "1":
        print("You have selected sockets.Fetching price...")
        break
    elif answer == "2":
        print("You have selected lights.Fetching price...")
        break
    elif answer == "3":
        print("You have selected switches.Fetching price...")
        break
    else:
        input("Please select one of the options above:")

    
