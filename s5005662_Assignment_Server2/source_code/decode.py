import s5005662_Assignment_Server2.received_files.decoder as dCR


def decode_text():
    decode_me_file = open("s5005662_Assignment_Server2/received_files/decode_me.txt", "r")
    coded_text = decode_me_file.read()
    print coded_text
    decoded_text = dCR.bin2utf(int(coded_text))
    print "The coded message in decode_me was: {}".format(decoded_text)
    decode_text_end(coded_text)


def decode_text_end(c_text):
    id_decode_bin = dCR.decodeID(c_text, "s5005662")
    print id_decode_bin
    print""
    id_decode_text = dCR.bin2utf(id_decode_bin)
    print id_decode_text




