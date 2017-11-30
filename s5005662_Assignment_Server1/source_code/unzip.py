import zipfile as zfile


def unzip_secret(pw):  # Unzips the file secret.zip using the password found using the program
    zf = zfile.ZipFile("s5005662_Assignment_Server1/received_files/secret.zip")
    zf.extractall("s5005662_Assignment_Server1/received_files", pwd=pw)
