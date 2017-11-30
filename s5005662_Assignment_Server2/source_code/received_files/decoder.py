def utf2bin(utf_string):
	bin_string = '{:b}'.format(int(utf_string.encode('utf-8').encode('hex'), 16))
	bin_string = int(bin_string,base=2)
	return bin_string
	
def bin2utf(bin_string):
	utf_string = bin(bin_string)[2:]
	utf_string = ('%x' % int(utf_string, 2)).decode('hex').decode('utf-8')
	return utf_string
	
def decodeID(encodedMessage, studentID):
	encodedMessage_bin = int(encodedMessage)
	studentID_bin_r = utf2bin(studentID[::-1])
	decodedMessage = encodedMessage_bin ^ studentID_bin_r
	return decodedMessage