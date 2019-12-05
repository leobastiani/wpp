#!python3
#encoding=utf-8
from __future__ import print_function, division, absolute_import

import argparse
import re
import os
import sys

parser = argparse.ArgumentParser(description='Open the door of my house')
parser.add_argument('numbers', nargs='*', help='números')
parser.add_argument('--debug', '-d', action='store_true', help='Debug mode')
args = parser.parse_args()

DEBUG = args.debug

def debug(*args):
    '''funciona como print, mas só é executada se sys.flags.debug == 1'''
    if not DEBUG:
        return ;
    print(*args)

debug("args:", args)

numbers = args.numbers

if not numbers:
    os.system("adb connect 192.168.0.241")
    # aqui eu abro o zap no meu celular
    os.system("adb shell am start -n com.whatsapp/com.whatsapp.Main")
    # botão de unlock
    os.system("adb shell input keyevent 82")
    # botão do espaço
    os.system("adb shell input keyevent 62")
    sys.exit(0)

debug("numbers:", numbers)
number = ''.join(numbers)
number = re.sub(r'\D+', '', number)
os.startfile("https://wa.me/%s" % number)