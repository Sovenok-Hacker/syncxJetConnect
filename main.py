from xjetpy import pyxJet
from xjetpy.constants import xJetNet
import asyncio
import json


api = pyxJet(
    api_key="API_KEY",
    private_key="PRIVATE_KEY", 
    mainnet=False
)


ton_address = ""
currency = ""
amount = 0
expires = 0
description = ""
activates_count = 0
groups_id = []
personal_id = ""
password = ""
cheque_id = ""
max_payments = 0
invoice_id = ""

api.me() # get API Application information.
api.balance() # get balance
api.submit_deposit() # check for deposit
api.withdraw(ton_address, currency, amount) # check for deposit

# Cheques methods
api.cheque_create(currency, amount, expires, description, activates_count, groups_id, personal_id, password) # create cheque
api.cheque_status(cheque_id) # get cheque status
api.cheque_list() # get cheques on account
api.cheque_cancel(cheque_id) # delete cheque

# Invoice methods
api.invoice_create(currency, amount, description, max_payments) # create invoice
api.invoice_status(invoice_id) # get invoice status
api.invoice_list() # get invoices on account


asyncio.run(main())