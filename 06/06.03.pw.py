PASSWORDS = {'email': 'jdaflkdjfl;akjjvjajdskfljafa',
             'blog': 'afkdlfjerjaf,jf.zf kad flk',
             'luggage': '12345'}

import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: python 06.03.pw.py [account]')
    print('copy the password to the clipboard')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('copy is done')
else:
    print(account + 'is not stored')