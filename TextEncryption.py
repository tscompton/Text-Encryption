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
        choice = raw_input("""

      Text Encryptor & Decryptor

        ----------------------
        |1) Encryption:      |
        |2) Decryption:      |
        |                    |
        |____________________|
        |h) Help             |
        |e) Exit             |
        |____________________|
        :""")
        if choice == "1":
            encryptionChoice = raw_input("""



        ----------------------
        |1) Base64:          |
        |2) cp037:           |
        |3) Ceasar-Cypther:  |
        |____________________|
        |h) Help             |
        |e) Exit             |
        |____________________|
        :""")
            if encryptionChoice == "1":
                encode("base64")
            elif encryptionChoice == "2":
                encode("cp037")
            elif encryptionChoice == "3":
                encode("rot_13")
            elif encryptionChoice == "h":
                helpMenu()
            elif encryptionChoice == "e":
                break
            else:
                print "Please try again"

        elif choice == "2":
            encryptionChoice = raw_input("""

        ----------------------
        |1) Base64:          |
        |2) cp037:           |
        |3) Ceasar-Cypther:  |
        |____________________|
        |h) Help             |
        |e) Exit             |
        |____________________|
        :""")

            if encryptionChoice == "1":
                decode("base64")
            elif encryptionChoice == "2":
                decode("cp037")
            elif encryptionChoice == "3":
                decode("rot_13")
            elif encryptionChoice == "h":
                helpMenu()
            elif encryptionChoice == "e":
                break
            else:
                print "Please try again"

        elif choice == "e":
            break
        elif choice == "h":
            helpMenu()

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


def helpMenu():
    print """\t     Choose either Encryption or Decryption by typing the
             corresponding number" and pressing enter.
             If doing encryption you will prompted to type a message to encrypt.
             Next choose the encryption type. You will be displayed your
             encrypted message and a text file will be made in the folder where
             this program lives. The text file will be named EncodedMessage.txt

             If doing decryption you will be prompted to choose encryption type.
             Next you will be prompted to enter the text file name.
             Be sure to type the whole file name and it must end in txt but can
             be named whatever.
             Example 'EncodedMessage.txt"
             You will be displayed the decoded message and a text file will be
             made with the decrypted message entitled DecodedMessage.txt
        """


main()

raw_input("Press any key to exit.")
