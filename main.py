# Pace
# V0LT
# Licensed under the GPLv3
# Version 0.9.1


# ----- Configuration -----

# Generate an API key in HealthBox with 'source' permissions and access to metric A1 (Steps), then input it here as a string. If this variable is left blank, Pace will ask you to enter your API key every time you run the program.
default_apikey = ""

# Enter the host address and port of your HealthBox instance here. For example, if you host HealthBox locally on the default port, enter `localhost:5050`. If this variable is left blank, Pace will ask you to enter your HealthBox server information every time you run the program.
default_server = ""



# This variable determines whether or not the URL will be printed when making the network request to HealthBox. This is extremely useful for debugging, but can be messy during normal usage.
url_debugging = False

# ----- End of Configuration -----


# Import required modules
import os
import time
import datetime 
from datetime import timezone
import traceback
import urllib.parse

# Attempt to import the 'requests' module
try:
    import requests
except ModuleNotFoundError as error:
    if traceback.format_exception_only (ModuleNotFoundError, error) != ["ModuleNotFoundError: No module named 'requests'\n"]: # Make sure the error we're catching is the right one
        raise # If not, raise the error
    raise utils.MissingLibraryError ("making web server requests", "requests")

    
 
# Define the function that will be used to clear the screen
def clear():
    if os.name == 'posix': # If the user is running MacOS or GNU/Linux
        _ = os.system('clear')
    else: # If the user is running Windows
        _ = os.system('cls')


# Define the function required to make network requests to HealthBox
class APICallError (Exception): pass # This will be used when returning errors.

def make_request (*, server, api_key, submission = None, print_url = False):
    endpoint = "metrics/a1/submit".split ('/') # Define the method and metric that this request will use on HealthBox.
    url = f"http://{server}/api/source/{'/'.join (endpoint)}?api_key={urllib.parse.quote (api_key)}" # Form the URL that will be used to communicate with HealthBox
    if submission is not None:
        url += f"&submission={urllib.parse.quote (submission)}" # Attach the JSON submission data to the URL formed above.
    if print_url: print (f"Making a request to {url}")
    response = requests.get (url) # Send the network request.
    response_data = response.json () # Save the response of the network request to the response_data variable.
    if not response_data ["success"]: # If something goes wrong, return an error.
        raise APICallError (response_data ["error"])
    del response_data ["success"]
    del response_data ["error"]
    return response_data


# Ask the user for the date they want to enter steps for
print("Please enter the date you'd like to submit steps for.")

while True: # Run forever until the user enters a valid day.
    day = int(input("Day: "))
    if (day >= 1 and day <= 31):
        break
    else:
        clear()
        print("Please enter a day that falls between 1 and 31.")

while True: # Run forever until the user enters a valid month.
    month = int(input("Month: "))
    if (month >= 1 and month <= 12):
        break
    else:
        clear()
        print("Please enter a month that falls between 1 and 12.")
       
while True: # Run forever until the user enters a valid year
    year = int(input("Year: "))
    if (year >= 1900):
        break
    else:
        clear()
        print("Please enter a year that falls past 1900.")
        


dt = datetime.date(year, month, day) # Combine the entered day, month, and year into a single variable.
timestamp = int(time.mktime(dt.timetuple())) # Convert the date to a Unix timestamp, so it can be submitted to HealthBox.



# Ask the user how many steps they'd like to submit for that date.
clear()
print("Please enter the number of steps you've taken on the entered date. Please note that this will be added to any steps already recorded for that date.")
while True: # Run forever until the user enters a valid day.
    steps = int(input("Steps: "))
    if (steps >= 0):
        break
    else:
        clear()
        print("Please enter an amount of steps that is positive.")



# Generate the submission data as plain text JSON data.
submission = '{"timestamp": ' + str(timestamp) + ', "data": {"steps_count": ' + str(steps) + ', "start_time": ' + str(timestamp) + ', "end_time": ' + str(timestamp) + '}}'



# Ask the user for their HealthBox instance information.
if (default_apikey == ""): # Check to see if the user has configured a preset API key in the configuration at the top of this script. If not, ask them to enter their API key.
    healthbox_apikey = input("Please enter a HealthBox API key for Pace.");
else: # If the user as configured an API key in the configuration at the top of this script, use that instead of asking them to enter one.
    healthbox_apikey = default_apikey

if (default_server == ""): # Check to see if the user has configured a preset HealthBox server address in the configuration at the top of this script. If not, ask them to enter the host and port for their HealthBox instance.
    healthbox_server = input("Please enter the server address, including the port, for your HealthBox instance: ")
else: # If the user has configured a HealthBox server address in the configuration at the top of this script, use that instead of asking them to enter one.
    healthbox_server = default_server

# Form and send the network request that will be used to submit the information to HealthBox using the make_request function.
response = make_request (server = healthbox_server, submission = submission, api_key = healthbox_apikey, print_url = url_debugging)
