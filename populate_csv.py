import pandas as pd
from datetime import datetime

names = ['Mainha e Davi', 'Flávio', 'Jordano', 'Rayza']
numbers = ['77988141042', '77991869698', '77988200611', '77991025521']
values = [14, 7, 28, 7]
dates = [datetime.today().strftime('%d/%m/%Y') for _ in range(4)]

contacts = {
    'name': names,
    'number': numbers,
    'value': values,
    'charge_date': dates
}
contacts = pd.DataFrame(contacts)
contacts.to_csv('contacts.csv', index=False)