# Xecryptor
# Copyright (c) 2015 Lykourgos Tanious
# Read LICENCE.txt
# XeCryptor cracker by most common character
# !!! THIS TOOL IS ONLY FOR EDUCATIONAL PURPOSES !!!
# creator   : Lykourgos Tanious
# date      : 09/02/2016
# Version   : V2.0


class XEcracker:

    def __init__(self, data):
        self.__cdata = []
        self.__cntlist = []
        self.__nlist = []
        self.__chlist = []
        self.__dec = []
        self.__decs = ""
        self.__data = data

    def crack(self):                                            # Cracks data returns decrypted text

        # Formating the data
        for item in self.__data:                                # Removes new line character (\n) from list
            self.__cdata.append(item.strip('\n'))
        self.__data = ""
        for item in self.__cdata:                               # Unites data to single string
            self.__data += item
        self.__cdata = []
        self.__cdata = self.__data.split(".")                   # Splits string to a list of values
        if self.__cdata[0] == '':                               # If first value is '' it is removed
            del self.__cdata[0]

        # Getting password
        llen = len(self.__cdata)                                # Gets the data length
        chars = llen / 3                                        # Gets the character length
        c = 0
        c1 = 0
        c2 = 1
        c3 = 2
        while True:                                             # Gets a list off character encrypted values
            if c < chars:                                       # by adding every three values
                self.__chlist.append(int(self.__cdata[c1])+int(self.__cdata[c2])+int(self.__cdata[c3]))
                c += 1
                c1 += 3
                c2 += 3
                c3 += 3
            else:
                break
        for item in self.__chlist:                              # Gets a list of unique items
            if self.__nlist.count(item) == 0:
                self.__nlist.append(item)
        for item in self.__nlist:                               # Gets a list with the number of unique items
            self.__cntlist.append(self.__chlist.count(item))
        mfc = self.__cntlist.index(max(self.__cntlist))         # Gets the index of the most frequent value
        mfc = self.__nlist[mfc]                                 # Gets the most frequent value
        passw = int(mfc) - 32

        # Decoding
        print()
        for item in self.__chlist:                              # Gets a list of decoded characters
            self.__dec.append(chr(int(item)-passw))
        for item in self.__dec:                                 # Converts the list to a string
            self.__decs += item
        return self.__decs       
