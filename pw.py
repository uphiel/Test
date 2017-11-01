#!/usr/bin/python3

PASSWORDS = {'email': 'pddiFeiEFievvIloe', 'blog': '2546879'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage:python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]
print("account:" + account)

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account name ' + account)

tableData = [['apples', 'oranges', 'cherries',
              'banana'], ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
# colWidths = [0] * len(tableData)
# print(colWidths)
length = 0

for Data in tableData:
    if isinstance(Data, list):
        for index, dData in enumerate(Data):
             if len(Data[index]) > length:
                length = len(Data[index]) 

print("length:" + str(length))

for Data in tableData:
    if isinstance(Data, list):
        for index, dData in enumerate(Data):
            if int(index) == (len(Data)-1):
                print(dData.rjust(length) + '')
            else:
                 print(dData.rjust(length), end=' ')