# Dash Button Wunderlist
## Installation
1. Install `scapy`
2. Install the other python requriements by running `pip install -r requirements.txt`
3. Find out the ethernet MAC address of your Dash by looking at your router's logs after pressing the Dash's button.  The ethernet MAC address will be a number that looks something like _74:c2:46:4a:52:af_.
4. Rename config_default.py to config.py
5. Edit config.py with your Wunderlist client ID and access token (visit http://developer.wunderlist.com to register your app and obtain these credentials).
6. Edit config.py to modify the _buttons_ dictionary with the MAC addresses of your Dash buttons and corresponding Wunderlist list and task names.  MAC addresses **must** be lowercase.
7. Run the script by executing `python dash.py`
8. After the script is running and says "Waiting for a button press...", press the Dash's button.
9. You should see a task added to your specified list.
10. CTRL-C exits the program.
