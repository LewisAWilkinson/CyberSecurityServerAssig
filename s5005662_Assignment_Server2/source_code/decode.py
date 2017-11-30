import s5005662_Assignment_Server2.received_files.decoder as dCR


def decode_text():
    decode_me_file = open("s5005662_Assignment_Server2/received_files/decode_me.txt", "r")
    coded_text = decode_me_file.read()
    print coded_text
    decoded_text = dCR.bin2utf(int(coded_text))
    print "The coded message in decode_me was: {}".format(decoded_text)
    decode_text_end(coded_text)


def decode_text_end(d_text):  # 46 chars before special message so 92 before
    d_text = d_text[92:]
    print d_text
    num = dCR.decodeID(d_text, "5005662")  # 85785046808565290219230888485608371060
    num1 = dCR.bin2utf(num)
    print num1



