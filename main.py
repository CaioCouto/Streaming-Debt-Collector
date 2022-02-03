import pandas as pd
import pywhatkit as kit
from time import sleep
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dotenv import dotenv_values

env = dotenv_values('.env')

def get_new_charge_date_str(charge_date, name):
    '''
        Increments x number of months to 
        the next charge date, based on the contact's name.
    '''
    new_charge_date = charge_date + relativedelta(months=5) if name == env['CONTACT_5M_RENEW'] else charge_date + relativedelta(months=1)
    return new_charge_date.strftime('%d/%m/%Y')

def send_message(contact_number, contact_name, contact_value, new_date):
    '''
        Sends the message a contact.
    '''
    kit.sendwhatmsg_instantly(
        f"+55{contact_number}",
        f'{contact_name}, o {env["STREAMING_SERVICE"]} venceu. Valor: R$ {contact_value},00\nMeu pix: {env["PAYMENT_NUMBER"]}\nPróximo pagamento: {new_date}',
        tab_close=True
    )

contacts = pd.read_csv('contacts.csv')
today = datetime.today()

for i in contacts.index:
    contact = contacts.iloc[i]
    contact_datetime = datetime.strptime(contact['charge_date'], '%d/%m/%Y')
    if today >= contact_datetime:
        new_charge_date_str = get_new_charge_date_str(contact_datetime, contact['name'])
        contacts.loc[i, 'charge_date'] = new_charge_date_str
        send_message(contact['number'], contact['name'], contact['value'], new_charge_date_str)
    sleep(1)

contacts.to_csv('contacts.csv', index=False)