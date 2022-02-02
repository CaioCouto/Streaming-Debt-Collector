import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pywhatkit as kit
from time import sleep

def get_new_charge_date_str(actual_date, name):
    new_charge_date = actual_date + relativedelta(months=5) if name == 'Jordano' else actual_date + relativedelta(months=1)
    return new_charge_date.strftime('%d/%m/%Y')

contacts = pd.read_csv('contacts.csv')
today = datetime.today()

for i in contacts.index:
    contact = contacts.iloc[i]
    contact_datetime = datetime.strptime(contact['charge_date'], '%d/%m/%Y')
    if today >= contact_datetime:
        new_charge_date_str = get_new_charge_date_str(contact_datetime, contact['name'])
        contacts.loc[i, 'charge_date'] = new_charge_date_str
        kit.sendwhatmsg_instantly(
            f"+55{contact['number']}",
            f'{contact["name"]}, o spotify venceu. Valor: R$ {contact["value"]},00\nMeu pix: 77991967081\nPróximo pagamento: {new_charge_date_str}',
            tab_close=True
        )
    sleep(1)

contacts.to_csv('contacts.csv', index=False)