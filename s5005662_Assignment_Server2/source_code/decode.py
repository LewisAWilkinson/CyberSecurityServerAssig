import s5005662_Assignment_Server2.received_files.decoder as dCR


def decode_text():
    decode_me_file = open("s5005662_Assignment_Server2/received_files/decode_me.txt", "r")
    coded_text = decode_me_file.read()
    print ""
    print "The coded message in decode_me is: {}".format(coded_text)
    decoded_text = dCR.bin2utf(int(coded_text))  # Using the binary ro utf decode function, the string is being decoded
    print ""
    print "The coded message in decode_me decodes to: {}".format(decoded_text)
    print ""
    double_decoding(coded_text)  # Passing the coded text from the file to the double decoding function


def double_decoding(c_text):
    id_decode_bin = dCR.decodeID(c_text, "s5005662")  # Using the id_decode function, the string is being decoded
    id_decode_text = dCR.bin2utf(id_decode_bin)  # Using the binary to utf decode function to decode the string further
    print id_decode_text  # Printing the result of the double decoding




