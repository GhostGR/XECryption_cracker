# Xecryptor 
# Copyright (c) 2015 Lykourgos Tanious
# Read LICENCE.txt
# XeCryptor cracker by most common character
# !!! THIS TOOL IS ONLY FOR EDUCATIONAL PURPOSES !!!
# creator   : Lykourgos Tanious
# date      : 11/1/2015


# Initialization of variables
cdata = []
cntlist = []
nlist = []
chlist = []
dec = []
decs = ""

# Menu
print()
print("############################")
print("#    XeCryption cracker    #")
print("#--------------------------#")
print("# Method : most common cha #")
print("#         racter space(32) #")
print("############################")
print()
filepath = input("Type the encrypted text file path :  ")

# Opening file
print("Opening file ...")
try:
    file = open(filepath, 'r')                                           # Opens file and adds lines to list
    data = file.readlines()
except:                                                                  # If it fails it displays a message and exits
    print("Failed to open file")
    print("Exiting...")
    exit()

# Formatting data
print("Formatting data ...")
for item in data:                                                        # Removes new line character (\n) from list
    cdata.append(item.strip('\n'))
data = ""
for item in cdata:                                                       # Unites data to single string
    data += item
cdata = []
cdata = data.split(".")                                                  # Splits string to a list of values
if cdata[0] == '':                                                       # If first value is '' it is removed
    del cdata[0]

# Getting password
print("Getting password...")
llen = len(cdata)                                                        # Gets the data length
chars = llen / 3                                                         # Gets the character lenght
c = 0
c1 = 0
c2 = 1
c3 = 2
while True:                                                              # Gets a list off character encrypted values
    if c < chars:                                                        # by adding every three values
        chlist.append(int(cdata[c1])+int(cdata[c2])+int(cdata[c3]))
        c += 1
        c1 += 3
        c2 += 3
        c3 += 3
    else:
        break
for item in chlist:                                                      # Gets a list of unique items
    if nlist.count(item) == 0:
        nlist.append(item)
for item in nlist:                                                       # Gets a list with the number of unique items
    cntlist.append(chlist.count(item))
mfc = cntlist.index(max(cntlist))                                        # Gets the index of the most frequent value
mfc = nlist[mfc]                                                         # Gets the most frequent value
passw = int(mfc) - 32                                                    # Gets the password value

# Decoding
print("Decrypting message ...")
print()
for item in chlist:                                                      # Gets a list of decoded characters
    dec.append(chr(int(item)-passw))
for item in dec:                                                         # Converts the list to a string
    decs += item
print(decs)
