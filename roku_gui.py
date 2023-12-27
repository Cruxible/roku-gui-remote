#!/usr/bin/env python3
#Created by: Ioannes Cruxibulum
#Date Created: 12-26-23

import gi
import time
import sys
import requests
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MySexyVariables:
    roku_ip = 'Your IP address'  # Replace with your Roku TV's IP address
    calls_list = [
                "youtube",
                "on",
                "off",
                "home",
                "vup",
                "vdown",
                "mute",
                "select",
                "play",
                "back",
                "up",
                "down",
                "left",
                "right",
                "exit"
                ]

    #Power Mode Strings
    power_mode_on = 'PowerOn'
    power_mode_off = 'PowerOff'
    power_mode_home = 'Home'
    power_mode_vol_up = 'VolumeUp'
    power_mode_vol_down = 'VolumeDown'
    power_mode_vol_mute= 'VolumeMute'
    power_mode_select = 'Select'
    power_mode_play = 'Play'
    power_mode_back = 'Back'
    power_mode_up = 'Up'
    power_mode_down = 'Down'
    power_mode_left = 'Left'
    power_mode_right = 'Right'

class Roku_Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Pyra Roku Remote")
        self.set_default_size(325, 400)
        fixed = Gtk.Fixed()
        self.add(fixed)

        on_button = Gtk.Button(label="Power On")
        on_button.set_size_request(40, 20)  # Set the width to 20 and the height to 20
        on_button.connect("clicked", self.on_button_clicked)
        fixed.put(on_button, 60, 10)  # Position the button at (10,50)

        off_button = Gtk.Button(label="Power Off")
        off_button.set_size_request(40, 20)  # Set the width to 20 and the height to 20
        off_button.connect("clicked", self.off_button_clicked2)
        fixed.put(off_button, 170, 10)  # Position the button at (10,50)

        up_button = Gtk.Button(label="Up")
        up_button.set_size_request(70, 20)  # Set the width to 20 and the height to 20
        up_button.connect("clicked", self.up_button_clicked)
        fixed.put(up_button, 125, 60)  # Position the button at (10,50)

        left_button = Gtk.Button(label="Left")
        left_button.set_size_request(40, 20)  # Set the width to 20 and the height to 20
        left_button.connect("clicked", self.left_button_clicked)
        fixed.put(left_button, 58, 100)  # Position the button at (10,50)

        select_button = Gtk.Button(label="Select")
        select_button.set_size_request(40, 20)  # Set the width to 20 and the height to 20
        select_button.connect("clicked", self.select_button_clicked)
        fixed.put(select_button, 125, 100)  # Position the button at (10,50)

        right_button = Gtk.Button(label="Right")
        right_button.set_size_request(40, 20)  # Set the width to 20 and the height to 20
        right_button.connect("clicked", self.right_button_clicked)
        fixed.put(right_button, 200, 100)  # Position the button at (10,50)

        down_button = Gtk.Button(label="Down")
        down_button.set_size_request(72, 20)  # Set the width to 20 and the height to 20
        down_button.connect("clicked", self.down_button_clicked)
        fixed.put(down_button, 125, 140)  # Position the button at (10,50)

        vol_down_button = Gtk.Button(label="< Vol")
        vol_down_button.set_size_request(40, 20)  # Set the width to 20 and the height to 20
        vol_down_button.connect("clicked", self.vol_down_button_clicked)
        fixed.put(vol_down_button, 55, 200)  # Position the button at (10,50)

        mute_button = Gtk.Button(label="Mute")
        mute_button.set_size_request(70, 20)  # Set the width to 20 and the height to 20
        mute_button.connect("clicked", self.mute_button_clicked)
        fixed.put(mute_button, 125, 200)  # Position the button at (10,50)

        vol_up_button = Gtk.Button(label="Vol >")
        vol_up_button.set_size_request(70, 20)  # Set the width to 20 and the height to 20
        vol_up_button.connect("clicked", self.vol_up_button_clicked)
        fixed.put(vol_up_button, 200, 200)  # Position the button at (10,50)

        home_button = Gtk.Button(label="Home")
        home_button.set_size_request(40, 20)  # Set the width to 20 and the height to 20
        home_button.connect("clicked", self.home_button_clicked)
        fixed.put(home_button, 125, 245)  # Position the button at (10,50)

        play_button = Gtk.Button(label="Play")
        play_button.set_size_request(70, 20)  # Set the width to 20 and the height to 20
        play_button.connect("clicked", self.play_button_clicked)
        fixed.put(play_button, 125, 288)  # Position the button at (10,50)

        back_button = Gtk.Button(label="Back")
        back_button.set_size_request(70, 20)  # Set the width to 20 and the height to 20
        back_button.connect("clicked", self.back_button_clicked)
        fixed.put(back_button, 125, 332)  # Position the button at (10,50)

        youtube_button = Gtk.Button(label="YT")
        youtube_button.set_size_request(40, 20)  # Set the width to 20 and the height to 20
        youtube_button.connect("clicked", self.youtube_button_clicked)
        fixed.put(youtube_button, 55, 332)  # Position the button at (10,50)

        exit_button = Gtk.Button(label="Exit")
        exit_button.set_size_request(40, 20)  # Set the width to 20 and the height to 20
        exit_button.connect("clicked", self.exit_button_clicked)
        fixed.put(exit_button, 200, 332)  # Position the button at (10,50)

    def on_button_clicked(self, button):
        payload = f'<?xml version="1.0" encoding="UTF-8"?><root><Power mode="{MySexyVariables.power_mode_on}"></Power></root>'
        response = requests.post(f'http://{MySexyVariables.roku_ip}:8060/keypress/{MySexyVariables.power_mode_on}', data=payload)
        # Check if the request was successful
        if response.status_code == requests.codes.ok:
            print(' Roku TV pressed power on button successfully')
        else:
            print(f' Failed to press power on button on Roku TV with error code: {response.status_code}')
    def off_button_clicked2(self, button):
        payload = f'<?xml version="1.0" encoding="UTF-8"?><root><Power mode="{MySexyVariables.power_mode_off}"></Power></root>'
        response = requests.post(f'http://{MySexyVariables.roku_ip}:8060/keypress/{MySexyVariables.power_mode_off}', data=payload)
        # Check if the request was successful
        if response.status_code == requests.codes.ok:
            print(' Roku TV pressed power off button successfully')
        else:
            print(f' Failed to press power off button on Roku TV with error code: {response.status_code}')
    def up_button_clicked(self, button):
        payload = f'<?xml version="1.0" encoding="UTF-8"?><root><Power mode="{MySexyVariables.power_mode_up}"></Power></root>'
        response = requests.post(f'http://{MySexyVariables.roku_ip}:8060/keypress/{MySexyVariables.power_mode_up}', data=payload)
        # Check if the request was successful
        if response.status_code == requests.codes.ok:
            print(' Roku TV pressed up button successfully')
        else:
            print(f' Failed to press up button on Roku TV with error code: {response.status_code}')
    def left_button_clicked(self, button):
        payload = f'<?xml version="1.0" encoding="UTF-8"?><root><Power mode="{MySexyVariables.power_mode_left}"></Power></root>'
        response = requests.post(f'http://{MySexyVariables.roku_ip}:8060/keypress/{MySexyVariables.power_mode_left}', data=payload)
        # Check if the request was successful
        if response.status_code == requests.codes.ok:
            print(' Roku TV pressed left button successfully')
        else:
            print(f' Failed to press left button on Roku TV with error code: {response.status_code}')
    def select_button_clicked(self, button):
        payload = f'<?xml version="1.0" encoding="UTF-8"?><root><Power mode="{MySexyVariables.power_mode_select}"></Power></root>'
        response = requests.post(f'http://{MySexyVariables.roku_ip}:8060/keypress/{MySexyVariables.power_mode_select}', data=payload)
        # Check if the request was successful
        if response.status_code == requests.codes.ok:
            print(' Roku TV pressed mute button successfully')
        else:
            print(f' Failed to press mute button on Roku TV with error code: {response.status_code}')
    def right_button_clicked(self, button):
        payload = f'<?xml version="1.0" encoding="UTF-8"?><root><Power mode="{MySexyVariables.power_mode_right}"></Power></root>'
        response = requests.post(f'http://{MySexyVariables.roku_ip}:8060/keypress/{MySexyVariables.power_mode_right}', data=payload)
        # Check if the request was successful
        if response.status_code == requests.codes.ok:
            print(' Roku TV pressed right button successfully')
        else:
            print(f' Failed to press right button on Roku TV with error code: {response.status_code}')
    def down_button_clicked(self, button):
        payload = f'<?xml version="1.0" encoding="UTF-8"?><root><Power mode="{MySexyVariables.power_mode_down}"></Power></root>'
        response = requests.post(f'http://{MySexyVariables.roku_ip}:8060/keypress/{MySexyVariables.power_mode_down}', data=payload)
        # Check if the request was successful
        if response.status_code == requests.codes.ok:
            print(' Roku TV pressed down button successfully')
        else:
            print(f' Failed to press down button on Roku TV with error code: {response.status_code}')
    def vol_down_button_clicked(self, button):
        for i in range(3):
            payload = f'<?xml version="1.0" encoding="UTF-8"?><root><Power mode="{MySexyVariables.power_mode_vol_down}"></Power></root>'
            response = requests.post(f'http://{MySexyVariables.roku_ip}:8060/keypress/{MySexyVariables.power_mode_vol_down}', data=payload)
            # Check if the request was successful
            if response.status_code == requests.codes.ok:
                print(' Roku TV pressed volume down button successfully')
            else:
                print(f' Failed to press volume down button on Roku TV with error code: {response.status_code}')
            time.sleep(.25)
    def mute_button_clicked(self, button):
        payload = f'<?xml version="1.0" encoding="UTF-8"?><root><Power mode={MySexyVariables.player_mode_vol_mute}"></Power></root>'
        response = requests.post(f'http://{MySexyVariables.roku_ip}:8060/keypress/{MySexyVariables.power_mode_vol_mute}', data=payload)
        # Check if the request was successful
        if response.status_code == requests.codes.ok:
            print(' Roku TV pressed mute button successfully')
        else:
            print(f' Failed to press mute button on Roku TV with error code: {response.status_code}')
    def vol_up_button_clicked(self, button):
        for i in range(3):
            # Construct the POST request payload to turn on the TV
            payload = f'<?xml version="1.0" encoding="UTF-8"?><root><Power mode="{MySexyVariables.power_mode_vol_up}"></Power></root>'
            response = requests.post(f'http://{MySexyVariables.roku_ip}:8060/keypress/{MySexyVariables.power_mode_vol_up}', data=payload)
            # Check if the request was successful
            if response.status_code == requests.codes.ok:
                print(' Roku TV pressed volume up button successfully')
            else:
                print(f' Failed to press volume up button on Roku TV with error code: {response.status_code}')
            time.sleep(.25)
    def home_button_clicked(self, button):
        payload = f'<?xml version="1.0" encoding="UTF-8"?><root><Power mode="{MySexyVariables.power_mode_home}"></Power></root>'
        response = requests.post(f'http://{MySexyVariables.roku_ip}:8060/keypress/{MySexyVariables.power_mode_home}', data=payload)
        # Check if the request was successful
        if response.status_code == requests.codes.ok:
            print(' Roku TV pressed home button successfully')
        else:
            print(f' Failed to press home button on Roku TV with error code: {response.status_code}')
    def play_button_clicked(self, button):
        payload = f'<?xml version="1.0" encoding="UTF-8"?><root><Power mode="{MySexyVariables.power_mode_play}"></Power></root>'
        response = requests.post(f'http://{MySexyVariables.roku_ip}:8060/keypress/{MySexyVariables.power_mode_play}', data=payload)
        # Check if the request was successful
        if response.status_code == requests.codes.ok:
            print(' Roku TV pressed play button successfully')
        else:
            print(f' Failed to press play button on Roku TV with error code: {response.status_code}')
    def back_button_clicked(self, button):
        payload = f'<?xml version="1.0" encoding="UTF-8"?><root><Power mode="{MySexyVariables.power_mode_back}"></Power></root>'
        response = requests.post(f'http://{MySexyVariables.roku_ip}:8060/keypress/{MySexyVariables.power_mode_back}', data=payload)
        # Check if the request was successful
        if response.status_code == requests.codes.ok:
            print(' Roku TV pressed back button successfully')
        else:
            print(f' Failed to press back button on Roku TV with error code: {response.status_code}')
    def youtube_button_clicked(self, button):
        try:
            app_url = f'http://{MySexyVariables.roku_ip}:8060/launch/837'
            response = requests.post(app_url)
        except requests.exceptions.HTTPError as e:
            print(f"Error launching app: {e}")
            print(f'Failed to send {action} command with error code: {response.status_code}')
    def exit_button_clicked(self, button):
        sys.exit()

win = Roku_Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
