#!python3
#encoding=utf-8
from __future__ import print_function, division, absolute_import

import argparse
import re
import os
import sys
import pyperclip
from urllib.parse import quote

def main():
    parser = argparse.ArgumentParser(description='Whatsapp link generator')
    parser.add_argument('--debug', '-d', action='store_true', help='Debug mode')
    parser.add_argument('--message', '-m', help='Message text')
    parser.add_argument('--copy', '-c', action='store_true', help='Copy url only')
    parser.add_argument('numbers', nargs='*', help='Whatsapp numbers')
    args = parser.parse_args()

    DEBUG = args.debug

    def debug(*args):
        '''funciona como print, mas só é executada se sys.flags.debug == 1'''
        if not DEBUG:
            return ;
        print(*args)

    debug("args:", args)

    numbers = args.numbers

    debug("numbers:", numbers)
    number = ''.join(numbers)
    number = re.sub(r'\D+', '', number)

    link = "https://wa.me/%s%s" % (number, f"?text={quote(args.message)}" if args.message else '')

    if args.copy:
        pyperclip.copy(link)
    else:
        os.startfile("https://wa.me/%s" % number)

if __name__ == '__main__':
    main()
