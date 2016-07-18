from actions import wunderlist, hue

# Wunderlist credentials
WUNDERLIST_CLIENT_ID =
WUNDERLIST_ACCESS_TOKEN =

# Hue info
HUE_BRIDGE_IP =
HUE_USER =

# Dash button actions
actions = {
    "12:34:56:ab:cd:ef": wunderlist.CreateTaskAction("Shopping", "Bar soap"),
    "34:56:78:cd:ef:ab": hue.SetSceneAction("Den", "Relax"),
    "90:12:34:ef:ab:cd": hue.ColorCycleAction("Den")
}