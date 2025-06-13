# OpenBali
Open source T-Dagger Bali keyboard driver software for linux. \
This script is reversed enginered T-Dagger's Bali keyboard USB protocol in action.

It ***should be fine*** running this script on other similar keyboard, since i captured usb packets with [T-TGK**305**'s software](https://www.t-dagger.com/pages/download) for my _T-TGK**311**_ keyboard (since t-dagger does not have any software for my keyboard).

If you are worried if it works or not, test if [Destroyer T-TGK305's software](https://www.t-dagger.com/pages/download) works for you. If not, I recommend not using this script[^1].

This script is tested on `T-TGK311-BL210400119`.

> [!CAUTION]
> I **CANNOT GARANTEE** THAT THIS SCRIPT WORKS FOR YOUR KEYBOARD IF MODEL IS NOT **EXACTLY** `T-TGK311-BL`. IF YOU BROKE YOUR KEYBOARD WITH THIS SCRIPT OR INSTRUCTIONS, I AM NOT RESPONSIBLE FOR YOUR ACTIONS. just saying.

## Instructions
1. Install PyUSB module:
```
pip install pyusb
```

2. Run the script as sudo

# TODO
[X] Make basic mode switch work
[X] Add settings for modes (only brightness and speed)
[X] Add color group support for "***Gaming Special Key***"
[ ] A setting for editing keys
[ ]   and adding macros
[ ] Add presets
[ ] Customizable "***Gaming Special Key***" profiles, Custom1(Fn+9) and Custom2(Fn+0)
[ ] Support for Windows (_god forbid_)


[^1]: When i was testing with different data and data length, my keyboard did not show any weired signs. so my guess is messing around with this script on other keyboards is fine.
