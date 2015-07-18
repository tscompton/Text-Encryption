#-------------------------------------------------------------------------------
# Name:        Text encoding and decoding
# Purpose:     A simple program used for encoded and decoding text
#              in various encryption methods.
#
# Author:      travis compton
#
# Created:     07/18/2015
# Copyright:   (c) travis compton 2015
# Licence:     The MIT License (MIT)
#-------------------------------------------------------------------------------



def main():
    while True:
        choice = raw_input("\t1:Encode:\n\t2:Decode:\n\t3:Exit:\n\t")
        if choice == "1":
            encryptionChoice = raw_input("Choose encryption type: \n1)Base64:\n2)cp037:\n3)Ceasar-Cypher:\n")
            if encryptionChoice == "1":
                encode("base64")
            elif encryptionChoice == "2":
                encode("cp037")
            elif encryptionChoice == "3":
                encode("rot_13")
            else:
                print "Please try again"

        elif choice == "2":
            encryptionChoice = raw_input("Choose decryption type: \n1)Base64:\n2)cp037\n3)Ceasar-Cypher:\n")
            if encryptionChoice == "1":
                decode("base64")
            elif encryptionChoice == "2":
                decode("cp037")
            elif encryptionChoice == "3":
                decode("rot_13")
            else:
                print "Please try again"

        elif choice == "3":
            break

        else:
            print "Unrecognized choice! Please type 1, 2, or 3."


#Function used to encode the text based on users encryption selection.
def encode(encryption):
    while True:
        message = raw_input("Type a message to encode:\n")
        encodedMessage = message.encode(encryption, "strict")
        encodedMessageText = open("EncodedMessage.txt", "w")
        encodedMessageText.write(encodedMessage)
        encodedMessageText.close()
        print "The enoded message is: ", encodedMessage
        break

#Function used to decode the text base on users decryption selection.
def decode(encryption):
    while True:
        encodedMessageText = raw_input("Type the name of the text file to decode or type 'e' to exit: ")
        high = len(encodedMessageText)
        if encodedMessageText[high -4:high] == ".txt":
            message = open(encodedMessageText, "r")
            readMessage = message.read()
            decodedMessage = readMessage.decode(encryption, "strict")
            decodedMessageText = open("DecodedMessage.txt", "w")
            decodedMessageText.write(decodedMessage)
            decodedMessageText.close()
            print "The decode message is: ", decodedMessage
            break
        elif encodedMessageText == "e":
            break
        else:
            print "The file name must be a .txt file and the extension must be typed!!"
            print "Example: 'EncodedMessage.txt' "


main()

raw_input("Press any key to exit.")
