import os
import matplotlib

def menu():
    print("")


def search_files():
    for root, dirs, files in os.walk("received_files/documents"):
        for eachfile in files:
            path = root + "/" + eachfile
            current_file = open(path, "r")
            encoded_text = current_file.read()
            decoded_text = encoded_text.decode(encoding="Hex")
            current_file.close()
            if "Millenium2000" in decoded_text:
                return decoded_text


def split_text():



print searchfiles()
