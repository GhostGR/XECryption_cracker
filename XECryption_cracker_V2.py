# Xecryptor
# Copyright (c) 2015 Lykourgos Tanious
# Read LICENCE.txt
# !!! THIS TOOL IS ONLY FOR EDUCATIONAL PURPOSES !!!
# Description :     This is the main script that uses the XEcracker.py
#               class to crack xecryption encrypted files.
# Author      : Lykourgos Tanious
# date        : 09/02/2016
# Version     : V2.0

# Imports
from XECracker import XEcracker

while True:
    print("################################################\n"            # Prints the main menu
          "#          XECryption cracking script          #\n"
          "#==============================================#\n"
          "#     Copyright (c) 2015 Lykourgos Tanious     #\n"
          "#----------------------------------------------#\n"
          "#   Version : V2.0                             #\n"
          "#   Author  : Lykourgos Tanious                #\n"
          "################################################\n")
    filepath = input("Input the encrypted file path :  ")
    try:
        file = open(filepath, 'r')                                        # Opens file and adds lines to list
        data = file.readlines()
    except:                                                               # If it fails it displays a message and exits
        print("Failed to open file")
        print("Exiting...")
        exit()
    cracker = XEcracker(data)                                             # Cracking file
    result = cracker.crack()
    print()
    print(result)                                                         # Printing the result
    print()
    while True:
        eq = input("Do you want to exit (yes/no)?   ")                    # Checks if user want to exit
        if eq == "yes" or eq == "YES" or eq == "Y":
            exit(0)
        elif eq == "no" or eq == "NO" or eq == "N":
            break
