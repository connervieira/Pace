# Pace

A simple way to enter your daily steps into your HealthBox database!

![Pace Logo](https://v0lttech.com/assets/img/pacelogo.png)
![Works with HealthBox](https://v0lttech.com/assets/img/workswithhealthbox.png)


## Usage

Pace is designed to work with HealthBox, and requires it to function. If you don't already have HealthBox, make sure to download and set it up before setting up Pace. It should also be noted that the following instructions assume you are on GNU/Linux. However, the same directions can be loosly followed for MacOS as well.

1. Download Pace, either from the V0LT website, or by clone the git repository using this command: `git clone https://github.com/connervieira/Pace`
2. Change into the newly downloaded Pace directory using the following command: `cd Pace`
3. Open the 'main.py' file with a text editor of your choice. For example, you may use the following command to open the file in a graphical text editor: `gedit main.py`
4. After opening the file, look for the section labled *Configuration*. This section stores the values you should change before running HealthBox.
5. Change the `default_apikey` variable to an API key generated in HealthBox for Pace. This API key should be a *source* key, and have permission to access metric A1 (Steps).
6. Change the `default_server` variable to the server host address and port number for your HealthBox instance. If you're running HealthBox locally, on the default port, this will likely be `localhost:5050`. However, if you're running HealthBox remotely, you may enter something more like `192.168.0.28:5050`.
7. Save and close the file.
8. Run `main.py` using Python 3, by running the following command: `python3 main.py`

You can now enter information about how many steps you took on a particular date using Pace! Every time you'd like to re-run Pace, simply navigate to the Pace folder and run `main.py`. After the initial set up, you shouldn't need to edit `main.py` again, unless you'd like to make changes to your configuration.


## Features

### Quick

After the initial configuration is complete, it's easy to add steps by date in a matter of seconds!

### Easy

Pace uses a simply terminal user interface that doesn't require you have an extensive knowledge of the command line. As long as you understand the basics, you'll have no problem running Pace!

### Completely Open Source

Just like HealthBox itself, Pace is completely open source from top to bottom, ensuring your privacy and security

### Well Documented

The source code of Pace is clearly laid out and well documented, making it easy to modify for other uses.

### Works With HealthBox

Pace works with HealthBox, the easy way to keep all of your health information in one secure, easy to access location!
