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
            if validate_password(user_name, password) == True:
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
    """ Allows the user to complete through the picklist """
    shipment_num = get_shipment_num()
    are_picks_available = check_picks_are_available(shipment_num)
    if are_picks_available == True:
        pick_list = get_pick_list(shipment_num)
        display_pick_to_user(pick_list)
        new_picking_sheet_data = update_new_pick_list(shipment_num)
        picking_sheet_worksheet.update(new_picking_sheet_data)
        select_program_function(user_name)
    else:
        print('No picks available for this shipment')
        select_program_function(user_name)
        
def check_picks_are_available(shipment_num):
    """
    checks that there are picks available for that shipment number.
    """
    pick_list = []
    for pick in picking_sheet_data:
        for item in pick:
            if item == shipment_num:
                pick_list.append(pick)
    for lists in pick_list:
        if lists[6] == 'unpicked':
            return True
        else: 
            return False
    
        
    
def get_shipment_num():
    """
    Gets the shipment nnumber from the user
    """
    shipment_num = input('Please enter the shipment number:\n')
    return(shipment_num)

def get_pick_list(shipment_num):
    """
    Gets picklist from the data sheet with the correct shipping number
    """
    pick_list = []
    for pick in picking_sheet_data:
        for item in pick:
            if item == shipment_num:
                pick_list.append(pick)
    print('Pick list retrieved')
    return(pick_list)

def display_pick_to_user(pick_list):
    """
    Dispay the pick to the user and validate the check code and item id.
    """
    while len(pick_list) >= 1:
        pick_list_2 = pick_list
        
        for lists in pick_list[:]:
            print('Current Pick is...')
            print(f'Item Description:{lists[1]}')
            print(f'Quantity Needed:{lists[2]}\n')
            print(f'Please go to:{lists[3]}\n')
            
            while True:
                check_code_inp = input('Please enter the check code for this location:\n')
                is_check_code_valid = validate_check_code(lists, check_code_inp)
                
                if is_check_code_valid:
                    print('Check code is valid!\n')
                    break
                else:
                    print('Check code is incorrect please try again...')
            while True:
                item_id_inp = input('Please enter the id for this item:\n')
                is_item_id_valid = validate_item_id(lists, item_id_inp)
                if is_item_id_valid:
                    print('Item id is valid!\n')
                    print('Item picked successfully')
                    break
                else:
                    print('Item id is incorrect please try again...')
            remove_pick_from_list(pick_list, lists)
        print('pick complete')

def update_new_pick_list(shipment_num):
    pick_list = get_pick_list(shipment_num)
    updated_pick_list = []
    print(pick_list)
    for lists in pick_list:
        lists[6] = 'picked'
        updated_pick_list.append(lists)
    print(updated_pick_list)
    new_pick_list = replace_pick_items_in_pick_list(pick_list, updated_pick_list)
    return(new_pick_list)
    
def replace_pick_items_in_pick_list(pick_list, updated_pick_list):
    """
    replacing pick list items
    """
    print('replacing items')
    for lists in pick_list:
        item_id = lists[0]
        item_shipping_number = lists[5]
        for lists_2 in updated_pick_list:
            item_id_2 = lists_2[0]
            item_shipping_number_2 = lists_2[5]
            if (item_id == item_id_2) and (item_shipping_number == item_shipping_number_2):
                picking_sheet_data.remove(lists)
                picking_sheet_data.append(lists_2)
                return picking_sheet_data

def remove_pick_from_list(pick_lists, lists):
    pick_lists.remove(lists)
    
def validate_check_code(pick, check_code):
    print('vaidating check code...')
    if pick[4] == check_code:
        return True
    else:
        return False
    
def validate_item_id(pick, item_id):
    print('vaidating item id...')
    if pick[0] == item_id:
        return True
    else:
        return False

def main():
    """
    Runs the program
    """
    user_name = request_login_data()
    program_function = select_program_function(user_name)
    if program_function == '1':
        picking_function(user_name)
    elif program_function == '2':
        put_away_function()

main()