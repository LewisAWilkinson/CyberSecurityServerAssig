import os
for root, dirs, files in os.walk("s5005662_Assignment_Server1/received_files/documents"):
    for eachfile in files:
        print eachfile
        currentFile = open(eachfile, "r")
        encodedText = currentFile.read()
        decodedText = encodedText.decode(encoding="Hex")
        print decodedText
        
