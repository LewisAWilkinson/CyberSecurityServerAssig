import socket						# Import socket module

s = socket.socket()					# Create a socket object		
host = "csmpop.ddns.net" 								# Type: string. The hostname of the machine
port = 	33331							# Type: number. The port running the service					# Connect to the specified host and port

s.connect((host, port))

student_id = "s5005662"						# Type: string. Your studentID e.g. i73543242

print "Requesting archive with ID: {}".format(student_id)
s.send(student_id)					# Sending the studentID to the service

# Create a file object to write to with the name 'received_files.zip'
f = open('received_files.zip','wb')	

# Start receiving and writing the data from the service
l = s.recv(1024)
while (l):
	print "Receiving..."
	f.write(l)
	l = s.recv(1024)

# Close the file
f.close()

print "Done Receiving"

# Shutdown and close the socket connection
s.shutdown(socket.SHUT_WR)
s.close()
