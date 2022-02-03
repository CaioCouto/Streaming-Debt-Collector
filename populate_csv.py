import pandas as pd
from datetime import datetime
from dotenv import dotenv_values

def create_csv_file(names, numbers, values, dates):
    '''
        Creates a dataframe and exports it to a csv file. 
    '''
    contacts = {
        'name': names,
        'number': numbers,
        'value': values,
        'charge_date': dates
    }
    pd.DataFrame(contacts).to_csv('contacts.csv', index=False)

env = dotenv_values('.env')
names, numbers, values = [v.split(', ') for v in env.values()]
dates = [datetime.today().strftime('%d/%m/%Y') for _ in range(4)]
create_csv_file(names, numbers, values, dates)