import requests
import os
import tkinter as tk
from tkinter import filedialog
import json

# Page Setup
root = tk.Tk()
root.withdraw()

layout = [    [tk.Label(text="Please enter the target IP address")],
    [tk.Entry()],
    [tk.Button(text="FETCH IP INFO"), tk.Button(text="SAVE INFO")],
    [tk.Text(width=30, height=10)],
    [tk.Label(text="Output format: "), tk.Radiobutton(text="JSON", variable=tk.StringVar(), value="json"),     tk.Radiobutton(text="CSV", variable=tk.StringVar(), value="csv"),     tk.Radiobutton(text="TXT", variable=tk.StringVar(), value="txt")],
    [tk.Button(text="Save as...")],
]

window = tk.Toplevel(root)
for i, row in enumerate(layout):
    for j, widget in enumerate(row):
        widget.grid(row=i, column=j)

ip_entry = layout[1][0]
output_text = layout[3][0]
output_format = layout[4][1:4]
save_as_button = layout[5][0]

# API Key
API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    API_KEY = tk.simpledialog.askstring("API Key", "Enter API Key from ipgeolocation.io")
    os.environ["API_KEY"] = API_KEY

# Data
data = {}

# Error handling
def handle_error(error):
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, error)
    output_text.config(state=tk.DISABLED)

# Fetch IP info
def fetch_ip_info():
    global data
    ip = ip_entry.get()
    link = f"https://api.ipgeolocation.io/ipgeo?apiKey={API_KEY}&ip={ip}"
    try:
        response = requests.get(link)
        if response.status_code == 200:
            data = response.json()
            country = data['country_name']
            state = data['state_prov']
            city = data['city']
            isp = data['isp']
            device = data['device_type']
            os = data['operating_system']
            network = data['network_name']
            info = "This IP is located in " + city + ", " + state + ", " + country + ", and is hosted by " + isp + "\n"
            info += "The device type is " + device + " and the operating system is " + os + "\n"
            info += "The IP belongs to the " + network + " network."
            output_text.config(state

