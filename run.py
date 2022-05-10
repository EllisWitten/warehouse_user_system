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

user_login_worksheet = SHEET.worksheet('user_login')
user_login_data = user_login_worksheet.get_all_values()

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
    all_user_names = []
    for data in user_login_data[1:]:
        all_user_names.append(data[0])
    if user_name in all_user_names:
        return True
    else:
        return False

def validate_password(user_name,password):
    for data in user_login_data:
        if data[0] == user_name:
            true_password = data[1]
            if password == true_password:
                return True

def select_program_function(user_name):
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
def main():
    user_name = request_login_data()
    program_function = select_program_function(user_name)
    if program_function == '1':
        picking_function()
    elif program_function == '2':
        put_away_function()

main()