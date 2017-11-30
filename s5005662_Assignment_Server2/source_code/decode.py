import os
import received_files.decode as dC


def decode_text():
    decode_me_file = open("received_files/decode_me", "r")
    coded_text = file.read()
    decoded_text = dC.bin2utf(coded_text)
    print decoded_text


decode_text()


