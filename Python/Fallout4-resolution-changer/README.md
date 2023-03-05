# Fallout 4 Screen Resolution Changer

## What is this?

As the name suggests, this is a scrip for changing Fallout 4's display resolution.

I wrote this to use on my Steam Deck to easily switch resolution in Gaming Mode.

## Usage

```
usage: fallout4-change-resolution.py [-h] [--width WIDTH] [--height HEIGHT] [--ini INI]

options:
  -h, --help       show this help message and exit
  --width WIDTH    The width value to be set.
  --height HEIGHT  The height value to be set.
  --ini INI        Fallout4Prefs.ini's location.
```

By default, this script will change the display resolution to `1280*800`, modifies 'Fallout4Prefs.ini' in Steam Deck's Fallout 4 proton prefix.

```
/home/deck/.steam/root/steamapps/compatdata/377160/pfx/drive_c/users/steamuser/Documents/My Games/Fallout4/Fallout4Prefs.ini
```
