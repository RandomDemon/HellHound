# Imports
import PySimpleGUI as UI
import requests

# Page Setup
UI.theme("Black")

layout = [
    [UI.Text("Please enter the target IP address")],
    [UI.Input()],
    [UI.Button("FETCH IP INFO"), UI.Button("SAVE INFO")],
    [UI.Output(size=(30, 10))],
]

window = UI.Window("IP INFO FETCHER", layout)

while True:
    event, values = window.read()
    if event == UI.WIN_CLOSED or event == "Exit":
        # Handles when the window is closed
        break
    elif event == "FETCH IP INFO":
        # Triggered when Fetch button is pressed
        ip = values[0]
        api = "6d6449bcef654c9089da3d2e2d8d817d" # Replace with your api key from --> https://ipgeolocation.io/
        link = "https://api.ipgeolocation.io/ipgeo?apiKey=" + api + "&ip=" + ip
        response = requests.get(link)
        if response.status_code == 200:
            # Formats the data
            data = response.json()
            country = data['country_name']
            state = data['state_prov']
            city = data['city']
            isp = data['isp']
            device = data['device_type']
            os = data['operating_system']
            network = data['network_name']
            data = "This IP is located in " + city + ", " + state + ", " + country + ", and is hosted by " + isp + "\n"
            data += "The device type is " + device + " and the operating system is " + os + "\n"
            data += "The IP belongs to the " + network + " network."
            # Prints the data
            print(data)
        else:
            # Handles when an error is encountered
            print("An error has occurred. Please try again")
    elif event == "Save Info":
        # Triggers when the save button is pressed
        file_path = UI.popup_get_file("Save IP Info as", save_as=True)
        with open(file_path, "w") as f:
            # Writes the data to a file
            f.write(data)

window.close()
