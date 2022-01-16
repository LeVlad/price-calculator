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


def back_to_menu():
    """
    A return to the main menu option that the user can use
    """
    while True:
        user_selection = input("Back to menu: B, Exit: E \n")
        if user_selection == "B" or user_selection == "b":
            start()
            break
        elif user_selection == "E" or user_selection == "e":
            exit_programme()
            break
        else:
            print("Invalid input, Try again")
            back_to_menu()
            break
        return False    

def get_sales_data():
    """
    Get sales figures input from the user.
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be three numbers, separated by commas.")
        print("Example: 10,20,30\n")

        data_str = input("Enter your data here: ")
        sales_data = data_str.split(",")
        validate_data(sales_data)
        
        if validate_data(sales_data):
            print("Data is valid!")
            update_worksheet(sales_data, "sales")
            back_to_menu()
        break


def update_worksheet(sales_data, worksheet):
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet("sales")
    worksheet_to_update.append_row(sales_data)
    print(f"{worksheet} worksheet updated successfully\n")

        
def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 3 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 3:
            raise ValueError(
                f"Exactly 3 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def get_quote():
    """
    Get quote information from user
    """
    print("""
        1.Sockets
        2.Lights
        3.Switches
        """)
    quote_answer = input("Please select which material you require a quote for:\n")
    if quote_answer == "1":
        print("""
        A.RCD
        B.Standard Switched
        C.Standard Unswitched
        """)
        socket_type = input("Please select the type of socket required\n:")
        
        if socket_type == "A" or socket_type == "a":
            sockets_price = SOCKETS.cell(2, 2).value
            sockets_price = int(float(sockets_price))
            sockets_quote = int(input("Please type in the amount of sockets\n:"))
            calculated_quote = sockets_quote * sockets_price
            total_amount = calculated_quote + ((calculated_quote*0.20))
            print(f'The sockets you require are {sockets_quote} and the total amount is:{total_amount}')
        elif socket_type == "B" or socket_type == "b":
            sockets_price = SOCKETS.cell(2, 3).value
            sockets_price = int(float(sockets_price))
            sockets_quote = int(input("Please type in the amount of sockets\n:"))
            calculated_quote = sockets_quote * sockets_price
            total_amount = calculated_quote + ((calculated_quote*0.20))
            print(f'The sockets you require are {sockets_quote} and the total amount is:{total_amount}')
        elif socket_type == "C" or socket_type == "c":
            sockets_price = SOCKETS.cell(2, 4).value
            sockets_price = int(float(sockets_price))
            sockets_quote = int(input("Please type in the amount of sockets\n:"))
            calculated_quote = sockets_quote * sockets_price
            total_amount = calculated_quote + ((calculated_quote*0.20))
            print(f'The sockets you require are {sockets_quote} and the total amount is:{total_amount}')
    elif quote_answer == "2":
        print("""
        A. Led batten
        B. Led ES bulb
        C. Led round bulkhead
        D. Led square bulkhead
        """)

        lights_type = input("Please select the type of lights required\n:")
        if lights_type == "A" or lights_type == "a":
            lights_price = LIGHTS.cell(2, 2).value
            lights_price = int(float(lights_price))
            lights_quote = int(input("Please type in the amount of lights\n:"))
            calculated_lights_quote = lights_quote * lights_price
            total_amount = calculated_lights_quote + ((calculated_lights_quote*0.20))
            print(f'The lights you require are {lights_quote} and the total amount is:{total_amount}')
        elif lights_type == "B" or lights_type == "b":
            lights_price = LIGHTS.cell(2, 3).value
            lights_price = int(float(lights_price))
            lights_quote = int(input("Please type in the amount of sockets\n:"))
            calculated_lights_quote = lights_quote * lights_price
            total_amount = calculated_lights_quote + ((calculated_lights_quote*0.20))
            print(f'The lights you require are {lights_quote} and the total amount is:{total_amount}')
        elif lights_type == "C" or lights_type == "c":
            lights_price = LIGHTS.cell(2, 4).value
            lights_price = int(float(lights_price))
            lights_quote = int(input("Please type in the amount of lights\n:"))
            calculated_lights_quote = lights_quote * lights_price
            total_amount = calculated_lights_quote + ((calculated_lights_quote*0.20))
            print(f'The lights you require are {lights_quote} and the total amount is:{total_amount}')
        elif lights_type == "D" or lights_type == "d":
            lights_price = LIGHTS.cell(2, 5).value
            lights_price = int(float(lights_price))
            lights_quote = int(input("Please type in the amount of lights\n:"))
            calculated_lights_quote = lights_quote * lights_price
            total_amount = calculated__lights_quote + ((calculated_lights_quote*0.20))
            print(f'The lights you require are {lights_quote} and the total amount is:{total_amount}')                
    elif quote_answer == "3":
        print("""
        A. Standard
        B. Dimmer
        C. Two way switch
        D. Intermediate
        """)

        switches_type = input("Please select the type of switch required\n:")
        if switches_type == "A" or switches_type == "a":
            switches_price = SWITCHES.cell(3, 2).value
            switches_price = int(float(switches_price))
            switches_quote = int(input("Please type in the amount of switches\n:"))
            calculated_switches_quote = switches_quote * switches_price
            total_amount = calculated_switches_quote + ((calculated_switches_quote*0.20))
            print(f'The switches you require are {switches_quote} and the total amount is:{total_amount}')
        elif switches_type == "B" or switches_type == "b":
            switches_price = SWITCHES.cell(3, 3).value
            switches_price = int(float(switches_price))
            switches_quote = int(input("Please type in the amount of switches\n:"))
            calculated_switches_quote = switches_quote * switches_price
            total_amount = calculated_switches_quote + ((calculated_switches_quote*0.20))
            print(f'The switches you require are {switches_quote} and the total amount is:{total_amount}')
        elif switches_type == "C" or switches_type == "c":
            switches_price = SWITCHES.cell(3, 4).value
            switches_price = int(float(switches_price))
            switches_quote = int(input("Please type in the amount of switches\n:"))
            calculated_switches_quote = switches_quote * switches_price
            total_amount = calculated_switches_quote + ((calculated_switches_quote*0.20))
            print(f'The switches you require are {switches_quote} and the total amount is:{total_amount}')
        elif switches_type == "D" or switches_type == "d":
            switches_price = SWITCHES.cell(3, 5).value
            switches_price = int(float(switches_price))
            switches_quote = int(input("Please type in the amount of switches\n:"))
            calculated_switches_quote = switches_quote * switches_price
            total_amount = calculated_switches_quote + ((calculated_switches_quote*0.20))
            print(f'The switches you require are {switches_quote} and the total amount is:{total_amount}')  
       
def exit_programme():
    """
    Shutting down program when user chose the exit task in menu
    """
    print("|*******************************************************|")
    print("|***************Thank you for using this****************|")
    print("|***********************APP!****************************|")
    print("|************************GOODBYE************************|")
    print("|*******************************************************|")

def start():
    """
    Start menu that the user can choose between 6 different tasks.
    """
    print("""
                --------MENU--------
                1. View sockets stock and price\n\
                2. View lights stock and price\n\
                3. View switches stock and price\n\
                4. Update sales\n\
                5. Get quote\n\
                6. Exit\n
                    """)
    while True:
        answer = input("Choose an option: \n")
        if answer == '1':
            print("Taking you to View sockets stock and price...\n")
            print("ALL PRICES ARE FOR SINGLE PARTS\n")
            socket_type = SOCKETS.col_values(1)
            socket_stock = SOCKETS.col_values(5)
            socket_price = SOCKETS.col_values(2)
            socket_size = SOCKETS.col_values(3)
            print(f'{socket_type}\n:{socket_size}\n:{socket_price}\n:{socket_stock}')
            back_to_menu()
            break
        elif answer == '2':
            print("Taking you to View lights stock and price......\n")
            print("ALL PRICES ARE FOR SINGLE PARTS\n")
            lights_type = LIGHTS.col_values(1)
            lights_wattage = LIGHTS.col_values(2)
            lights_price = LIGHTS.col_values(3)
            lights_stock = LIGHTS.col_values(4)
            print(f'{lights_type}\n:{lights_wattage}\n:{lights_price}\n:{lights_stock}')
            back_to_menu()
            break
        elif answer == '3':
            print("Taking you to View switches stock and price......\n")
            print("ALL PRICES ARE FOR SINGLE PARTS\n")
            switches_type = SWITCHES.col_values(1)
            switches_price = SWITCHES.col_values(3)
            switches_stock = SWITCHES.col_values(4)
            print(f'{switches_type}\n:{switches_price}\n:{switches_stock}')
            back_to_menu()
            break
        elif answer == '4':
            print("Taking you to Update sales...\n")
            get_sales_data()
            back_to_menu()    
            break
        elif answer == '5':
            print("Taking you to Get quote...\n")
            get_quote()
            back_to_menu()
            
            break
        elif answer == '6':
            print("Exiting...")
            exit_programme()
            break
        else:
            print("Not a valid input please enter a number 1-6")

def main():
    """
    Function that runs all functions
    """
    start()

main()
