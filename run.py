import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('warehouse_user_system')

global_shipment_num = ''
user_login_worksheet = SHEET.worksheet('user_login')
user_login_data = user_login_worksheet.get_all_values()
picking_sheet_worksheet = SHEET.worksheet('picking_sheet')
picking_sheet_data = picking_sheet_worksheet.get_all_values()

def request_login_data():
    """
    Get user name and password
    """
    while True:
        print('Welcome to the Warehouse User Software.')
        print('PLease enter your username and password ...\n')
        user_name = input('Username:\n')
        password = input('Password:\n')
        
        if validate_user_name(user_name) == True:
            print('Username is accepted')
            if validate_password(user_name,password) == True:
                print('Password Accepted')
                return user_name
                break
            else:
                print('Password is incorrect')
        else:
            print('Username is incorrect')
    
def validate_user_name(user_name):
    """
    Checks the sername given matches on in the database
    """
    all_user_names = []
    for data in user_login_data[1:]:
        all_user_names.append(data[0])
    if user_name in all_user_names:
        return True
    else:
        return False

def validate_password(user_name,password):
    """
    Checks the pasowrd is corrct for the username given
    """
    for data in user_login_data:
        if data[0] == user_name:
            true_password = data[1]
            if password == true_password:
                return True

def select_program_function(user_name):
    """
    Allows the user to pick which function they want the program to run and execute it
    """
    print(f'\nWelcome back {user_name}\n')
    while True:
        print('1)Picking')
        print('2)Put Away')
        print('3)Log Out')
        program_function = input('\nPlease enter either 1,2 or 3:\n')
        if program_function == '1':
            return program_function
            break
        elif program_function == '2':
            return program_function
            break
        elif program_function == '3':
            print(f'Goodbye {user_name}')
            exit()
        else:
            print('Please enter a valid option')

def picking_function(user_name):
    """
    
    """
    if len(picking_sheet_data) == 1:
        print('\nNo picks avalible')
        print()
        select_program_function(user_name)
    
    shipment_num = input('Please enter the shipment number:\n')
    pick_list = get_picks_from_shipment(shipment_num)
    if len(pick_list) >= 1:
        print('picks found')
        print(shipment_num)
        user_picking(pick_list, shipment_num)
    else:
        print('no picks found')
        exit()

def get_picks_from_shipment(shipment_num):
    picking_sheet = []
    for data in picking_sheet_data:
        for element in data:
            if element == shipment_num:
                picking_sheet.append(data)
    return picking_sheet

def user_picking(pick_list, shipment_num):
    while len(pick_list) >= 1:
        for lists in pick_list[:]:
            print(f'Item location is: {lists[3]}\n')
            while True:
                item_check_code_inp = input(print('\nPlease enter the location check code:\n'))
                if item_check_code_inp == lists[4]:
                    print('check code is correct\n')
                    break
                elif (item_check_code_inp == 'exit'):
                    exit()
                else:
                    print('check code is incorrect please try again.\n')
            print(f'You need to pick {lists[2]} of these items')
            while True:
                item_id_inp = input(print('Please enter the item id...'))
                if item_id_inp == lists[0]:
                    print('Pick complete')
                    pick_list.pop(0)
                    print('returning 1')
                    break
                elif (item_id_inp == 'exit'):
                    print('exit')
                    exit()
                else:
                    print('Item id incorrect please try again')
            print('returning 3')
            print(shipment_num)
            global global_shipment_num
            global_shipment_num = shipment_num
 
def update_pick_status(shipment_num):
    print('updating pick status...')
    print(picking_sheet_data)
    picked_list = []
    for data in picking_sheet_data:
        for element in data:
            if element == shipment_num:
                data[6] = 'picked'
                picked_list.append(data)
    print(picked_list)

def main():
    user_name = request_login_data()
    program_function = select_program_function(user_name)
    if program_function == '1':
        picking_function(user_name)
        update_pick_status(global_shipment_num)
    elif program_function == '2':
        put_away_function()

main()