# OpenBali
Open source T-Dagger Bali keyboard driver software for linux. \
This script is reversed enginered T-Dagger's Bali keyboard USB protocol in action.

It ***should be fine*** running this script on other similar keyboard, since i captured usb packets with [T-TGK**305**'s software](https://www.t-dagger.com/pages/download) on my _T-TGK**311**_ keyboard[^1] (since t-dagger does not have any software for my keyboard).

If you are worried if it works or not, test if [Destroyer T-TGK305's software](https://www.t-dagger.com/pages/download) works for you. If not, I recommend not using this script[^2].

> [!CAUTION]
> I **CANNOT GARANTEE** THAT THIS SCRIPT WORKS FOR YOUR KEYBOARD IF MODEL IS NOT **EXACTLY** `T-TGK311-BL`. IF YOU BROKE YOUR KEYBOARD WITH THIS SCRIPT OR INSTRUCTIONS, I AM NOT RESPONSIBLE FOR YOUR ACTIONS. just saying.

This project could become an open keyboard driver software! It just needs YOUR help. you can do these steps to contribute:
1. open your keyboard software
2. Start capturing usb packets with wireshark in usbcap mode.
3. Apply every possible configuration you can for your keyboard in the driver software.
4. Stop the recording and write **Your exact keyboard model**, **Which software did you use along with exact version** and **upload the capture file** in github issues.
This way, the packets that sets the keyboards settings gets captured and i can use it to make settings for it.
Or, you know, write your kb's protocol in python and open a PR to merge it to the script.


## Instructions
1. Make a virtual enviornment and activate it to install packages:
```
uv env
source .env/bin/activate
```

2. Install PyUSB module:
```
pip install pyusb
```

3. Run the script with sudo:
```
sudo python main.py
```


## How protocol works
These are the packets that the software sends:

| **order** 	| **length** 	| **name**           	| **description**                     	| **when to send**                  	|
|-----------	|------------	|--------------------	|-------------------------------------	|-----------------------------------	|
| 1         	| ~80b       	| Mode data          	| which mode with which settings      	| sent always                       	|
| 2         	| ~1900b     	| Macro data         	| sends all macro to keyboard         	| sent only when macro data changes 	|
| 3         	| ~540b      	| Key remapping data 	| which data to send when key pressed 	| sent always                       	|
|           	|            	|                    	|                                     	|                                   	|

## TODO
- [X] Make basic mode switch work
- [X] Add settings for modes (only brightness and speed)
- [X] Add color group support for "***Gaming Special Key***"
- [ ] Adding key macros and key remapping
- [ ] Change code structure so it would be easy to add another keyboard support
- [ ] Add config file to save keyboard id (prevent searching for compatible keyboard each time), store profiles, presets and last mode used
- [ ] Add presets
- [ ] Customizable lights for "***Gaming Special Key***" custom profiles
- [ ] GUI support
- [ ] Support for Windows (_god forbid_)


[^1]: exact serial number of the keyboard: `T-TGK311-BL210400119`.
[^2]: When i was testing with different data and data length, my keyboard did not show any weired signs. so my guess is messing around with this script on other keyboards is fine. the worse that did happen during testing was that the leds turned off, but the keys were still working and i did manage to switch to another mode 
