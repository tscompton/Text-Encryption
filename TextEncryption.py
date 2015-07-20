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
import hashlib


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
        |4) MD5:             |
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
            elif encryptionChoice == "4":
                processChoice = raw_input("1) Hash a message: \n2) Hash a file:\nh) Help: \ne) Exit:\n")
                if processChoice == "1":
                    encodeHash("1", "MD5")
                elif processChoice == "2":
                    encodeHash("2", "MD5")
                elif processChoice == "h":
                    helpMenu("md5")
                elif processChoice == "e":
                    break
                else:
                    print "Invalid choice, Please try again"
            elif encryptionChoice == "h":
                helpMenu("general")
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
                helpMenu("general")
            elif encryptionChoice == "e":
                break
            else:
                print "Please try again"

        elif choice == "e":
            break
        elif choice == "h":
            helpMenu("general")

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


def helpMenu(helpType):
    if helpType == "general":
        print """\t         Choose either Encryption or Decryption by typing the
                 corresponding number" and pressing enter.
                 If doing encryption you will prompted to type a message to
                 encrypt. Next choose the encryption type. You will be
                 displayed your encrypted message and a text file will be made
                 in the folder where this program lives. The text file will be
                 named EncodedMessage.txt

                 If doing decryption you will be prompted to choose encryption
                 type. Next you will be prompted to enter the text file name.
                 Be sure to type the whole file name and it must end in txt but
                 can be named whatever.
                 Example 'EncodedMessage.txt"
                 You will be displayed the decoded message and a text file will
                 be made with the decrypted message entitled DecodedMessage.txt
            """
    elif helpType == "md5":
        print """\t         Choose either to hash a message or hash a file.
                 If hashing a message, input your message and the MD5 hash
                 will be displayed and a text file will be made created as
                 'HashedMessageMD5.txt'.
                 If hashing a file input the name of the file to be hashed,
                 note the file must be in the same directory as this program.
                 Exampe 'ThisFile.exe'
                 The hash for the file will be displayed and a text file will
                 be created in the same folder as this program named
                 MD5FileChecksum.txt
              """


def encodeHash(choice, method):
    if choice == "1" and method == "MD5":
        message = raw_input("Type a message to encode in MD5 :\n")
        a = hashlib.md5()
        a.update(message.encode('utf-8'))
        encodedMessageText = open("HashedMessageMD5.txt", "w")
        encodedMessageText.write(a.hexdigest())
        encodedMessageText.close()
        print a.hexdigest()

    elif choice == "2" and method == "MD5":
        fileName = raw_input('Enter file name: ')
        fileHash = hashlib.md5(open(fileName, 'rb').read()).hexdigest()
        fileHashText = open("MD5FileChecksum.txt", "w")
        fileHashText.write(fileHash)
        fileHashText.close()
        print fileHash



main()

raw_input("Press any key to exit.")
