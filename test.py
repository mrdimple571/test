# Everything Come back with Json and Convert to Python Dictionary 

# Import Python Modules
import yaml
import base64
import json

# Import Check Point SDK
from cpapi import APIClientArgs, APIClient

# Loading YML Credential File (Base64)
credentials = yaml.load(open('/home/chris/cp_mgmt_api_python_sdk/tasks/cred.yml'))

# Converting Base64 to UTF-8 and Saving to Variable
b64_user = credentials['user']
b64_password = credentials['password']
user = base64.b64decode(b64_user).decode('utf-8')
password = base64.b64decode(b64_password).decode('utf-8')

# Asking User for CMA IP
cma = input("Enter CMA IP :")

# Connect with the CMA
client_args = APIClientArgs(server=cma)
session = APIClient(client_args)
login_response = session.login(user, password, domain=cma)
print(login_response) 

# Run the API Call - Look at Web Services! 

# Check Session Changes 
session.api_call(

#Logout of CMA
session.api_call("logout")
