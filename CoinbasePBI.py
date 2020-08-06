# Imports
import config #Remove this in PowerBI
import pandas as pd
from coinbase.wallet.client import Client

# Variables
api_key = config.api_key #Replace 'config.api_key' with your APIkey
api_secret = config.api_secret #Replace 'config.api_secret' with your APIsecret
endpoint = 'accounts' #Choose betweeen 'accounts', 'transactions', 'buys', 'sells'

#Connect
client = Client(api_key, api_secret)

#Account ID List
input_accountid = [client.get_accounts()][0]['data']
accountid_array = [client.get_primary_account()['id']]
for item in input_accountid:
    accountid = item.id
    accountid_array.append(accountid)

# Get endpoint data
input_data = []

if endpoint == 'accounts':
    input_primary = [client.get_primary_account()][0]
    input_data.append(input_primary)
    for item in input_accountid:
        input_item = item
        input_data.append(input_item)

else:
    for accountid in accountid_array:
        item_string = "[client.get_"+endpoint+"('"+accountid+"')][0]['data']"
        input_item = eval(item_string)

        for item in input_item:
            b = item
            b['accountid'] = accountid
            input_data.append(b)

# Output data
output_data = pd.DataFrame(input_data)
print(output_data)
