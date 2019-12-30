import getpass
import logging
import json
import base64
from termcolor import colored

# Import Check Point SDK
from cpapi import APIClientArgs, APIClient

# Create and Configure Script Logger
logging.basicConfig(
        filename = "/home/chris/cp_mgmt_api_python_sdk/tasks/log/show-networks.json",
        level = logging.INFO,
        format = "%(levelname)s:%(asctime)s:%(message)s"
        )
logger = logging.getLogger()

# Variables for the Python Script:
color = "green"

# Variables for API Query:
api_query = 'show-networks'
details = "full"

# Requesting Data from User
print("")
cma = input("Enter the CMA IP: ")
user = input("Enter your Username: ")
password = getpass.getpass("Enter password (Hidden): ")
print("")

# Passing User Data to Check Point SDK
client_args = APIClientArgs(server=cma)
session = APIClient(client_args)

# Logging into CMA
login_response = session.login(user, password, domain=cma)
print(colored("Login Response:", color))
print(login_response)
logger.info(login_response)

# Redirect Output and Logging Out of CMA
print("")
print(colored("Redirecting API Output to File:", color))
query = session.api_query(api_query, details_level=details)

# Setting Up a Dictionary for the Query Data
query_dict={}



# logger.info(query)
# print("/home/chris/cp_mgmt_api_python_sdk/tasks/log/show-networks.json")
# print("")

# Logging out of CMA
print(colored("Logout Response:", color))
logout_response = session.api_call("logout")
print(logout_response)
logger.info(logout_response)
