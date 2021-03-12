# Pace
# V0LT
# Licensed under the GPLv3
# Version 0.1



# ----- Configuration -----

# Generate an API key in HealthBox with 'source' permissions and access to metric A1 (Steps), then input it here as a string. If this variable is left blank, Pace will ask you to enter your API key every time you run the program.
default_apikey = ""

# Enter the host address and port of your HealthBox instance here. For example, if you host HealthBox locally on the default port, enter `localhost:5050`. If this variable is left blank, Pace will ask you to enter your HealthBox server information every time you run the program.
default_server = ""


# ----- End of Configuration -----



import time
import datetime 
from datetime import timezone
import traceback
import urllib.parse

# Attempt to import the requests library
try:
    import requests
except ModuleNotFoundError as error:
    if traceback.format_exception_only (ModuleNotFoundError, error) != ["ModuleNotFoundError: No module named 'requests'\n"]: # Make sure the error we're catching is the right one
        raise # If not, raise the error
    raise utils.MissingLibraryError ("making web server requests", "requests")


# Define the function required to make network requests to HealthBox
class APICallError (Exception): pass

def make_request (*, server, api_key, submission = None, print_url = False):
    endpoint = "metrics/a1/submit".split ('/')
    url = f"http://{server}/api/source/{'/'.join (endpoint)}?api_key={urllib.parse.quote (api_key)}"
    if submission is not None:
        url += f"&submission={urllib.parse.quote (submission)}"
    if print_url: print (f"Making a request to {url}")
    response = requests.get (url)
    response_data = response.json ()
    if not response_data ["success"]:
        raise APICallError (response_data ["error"])
    del response_data ["success"]
    del response_data ["error"]
    return response_data




# Ask the user for the date they want to enter steps for
print("Please enter the date you'd like to submit steps for.")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))


dt = datetime.date(year, month, day) # Combine the entered variables into a single variable.
timestamp = int(time.mktime(dt.timetuple())) # Convert the date to a Unix timestamp, so it can be submitted to HealthBox.



# Ask the user how many steps they'd like to submit for that date.
steps = int(input("Please enter the number of steps you've taken on that date. Please note that this will be added to any steps already recorded for that date: "))


# Generate the submission data as plain text JSON data, then encode it to be used as a URL
submission = '{"timestamp": ' + str(timestamp) + ', "data": {"steps_count": ' + str(steps) + ', "start_time": ' + str(timestamp) + ', "end_time": ' + str(timestamp) + '}}'



# Ask the user for their HealthBox instance information.
if (default_apikey == ""): # Check to see if the user has configured a preset API key. If not, ask them to enter their API key.
    healthbox_apikey = input("Please enter a HealthBox API key for Pace.");
else:
    healthbox_apikey = default_apikey

if (default_server == ""): # Check to see if the user has configured a preset HealthBox server address. If not, ask them to enter the host and port for their HealthBox instance.
    healthbox_server = input("Please enter the server address, including the port, for your HealthBox instance: ")
else:
    healthbox_server = default_server

# Form the network request that will be used to submit the information to HealthBox.
response = make_request (server = healthbox_server, submission = submission, api_key = healthbox_apikey, print_url = True)
