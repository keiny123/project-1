from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from datetime import datetime  # Import datetime module for date and time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Define your Google Sheets credentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
# Replace the path below with the path to your JSON key file
creds = ServiceAccountCredentials.from_json_keyfile_name('D:\kenneth priorities\MARK BUSINESS APP\APP\excel-app-416205-fb140453c87f.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheets spreadsheet by name
spreadsheet = client.open('Daily Tracker')

# Inspector accounts
inspectors = {
    'inspector1': 'password1',
    'inspector2': 'password2',
    'inspector3': 'password3',
    'inspector4': 'password4'
}

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        
        self.username_input = TextInput(hint_text='Username')
        layout.add_widget(self.username_input)
        
        self.password_input = TextInput(hint_text='Password', password=True)
        layout.add_widget(self.password_input)

        # Label to display current date and time
        self.datetime_label = Label(text='')
        layout.add_widget(self.datetime_label)
        
        login_button = Button(text='Login')
        login_button.bind(on_press=self.login)
        layout.add_widget(login_button)
        
        self.add_widget(layout)
        
        self.update_datetime()  # Update date and time when the screen is initialized

    def update_datetime(self):
        self.current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.datetime_label.text = f'Current Date and Time: {self.current_datetime}'

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        
        if username in inspectors and inspectors[username] == password:
            self.manager.current = 'main'
        else:
            print('Invalid username or password')

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        
        # Input fields for item number and quantity
        item_number_label = Label(text='Enter item number:')
        layout.add_widget(item_number_label)
        self.item_number_input = TextInput()
        layout.add_widget(self.item_number_input)
        
        quantity_label = Label(text='Enter quantity:')
        layout.add_widget(quantity_label)
        self.quantity_input = TextInput()
        layout.add_widget(self.quantity_input)
        
        # Button to submit input
        submit_button = Button(text='Submit')
        submit_button.bind(on_press=self.submit_input)
        layout.add_widget(submit_button)
        
        self.add_widget(layout)
    
    def submit_input(self, instance):
        # Get input values
        item_number = self.item_number_input.text
        quantity = self.quantity_input.text
        
        # Get the current inspector from the username input
        current_inspector = self.manager.get_screen('login').username_input.text

        # Get the current date and time from the LoginScreen
        current_datetime = self.manager.get_screen('login').current_datetime

        # Get the corresponding sheet for the inspector
        if current_inspector in inspectors:
            sheet = spreadsheet.worksheet(current_inspector)
        else:
            print('Invalid inspector.')
            return

        # Append item number to row B and quantity to row C along with the current date and time
        row_index = len(sheet.col_values(1)) + 1
        sheet.update_cell(row_index, 1, current_datetime)  # Update date and time in column A
        sheet.update_cell(row_index, 2, item_number)       # Update item number in column B
        sheet.update_cell(row_index, 3, quantity)          # Update quantity in column C

        print(f"Item number '{item_number}' and quantity '{quantity}' submitted to Google Sheets for inspector {current_inspector} at {current_datetime}")

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    MyApp().run()
