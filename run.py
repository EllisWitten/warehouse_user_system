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
        user_name = input('Username:')
        password = input('Password:')
        
        if validate_user_name(user_name) == True:
            print('Username is accepted')
            if validate_password(user_name,password) == True:
                print('Password Accepted')
                print(f'Welcome {user_name}')
                break
        else:
            print('Password or username was inccorect')
    
def validate_user_name(user_name):
    all_user_names = []
    for data in user_login_data[1:]:
        all_user_names.append(data[0])
    if user_name in all_user_names:
        return True
    else:
        print('Username is incorrect')
        return False

def validate_password(user_name,password):
    for data in user_login_data:
        if data[0] == user_name:
            true_password = data[1]
            if password == true_password:
                return True
def main():
    request_login_data()

main()