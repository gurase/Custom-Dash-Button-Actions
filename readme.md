# Dash Button Custom Actions
## About
I purchased a bunch of Amazon Dash buttons to do a few different things. Most of them I use to add items to my shared shopping list in Wunderlist. Some I set up to control my Philips Hue lights. This app handles all those actions and makes it easy to add additional ones.
## Installation
1. Install `scapy`
2. Install the other python requirements by running `pip install -r requirements.txt`
3. Find out the ethernet MAC address of your Dash by looking at your router's logs after pressing the Dash's button.  The ethernet MAC address will be a number that looks something like _74:c2:46:4a:52:af_.
4. Rename config_default.py to config.py
5. Edit config.py with any API credentials you might need. Examples are provided for Wunderlist and Philips Hue.
6. Edit config.py to modify the _actions_ dictionary with the MAC addresses (**must** be lowercase) of your Dash buttons and corresponding actions. Several Wunderlist and Philips Hue actions are provided in the actions module. Any additional actions must implement the base Action class.
7. Run the script by executing `python dash.py`
8. After the script is running and says "Waiting for a button press...", press the Dash's button.
9. You should see your action execute.
10. CTRL-C exits the program.
