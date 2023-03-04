import configparser
import argparse
import tkinter as tk
from tkinter import messagebox

parser = argparse.ArgumentParser()
parser.add_argument('--width', help='The width value to be set.', default='1280')
parser.add_argument('--height', help='The height value to be set.', default='800')
parser.add_argument('--ini', default='/home/deck/.steam/root/steamapps/compatdata/377160/pfx/drive_c/users/steamuser/Documents/My Games/Fallout4/Fallout4Prefs.ini', help="Fallout4Prefs.ini's location.")
args = parser.parse_args()

config = configparser.ConfigParser()
config.optionxform = lambda option: option
config.read(args.ini)
config['Display']['iSize H'] = args.height
config['Display']['iSize W'] = args.width
with open(args.ini, 'w') as f:
    config.write(f)

root = tk.Tk()
root.withdraw()
messagebox.showinfo(title='Done.', message='Change resolution to {}*{}.'.format(args.width, args.height))
