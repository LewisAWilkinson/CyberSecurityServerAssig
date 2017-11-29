import zipfile as zfile


def unzip_secret(pw):  # Unzips the file secret.zip using the password found using the program
    zf = zfile.ZipFile("received_files/secret.zip")
    zf.extractall("received_files", pwd=pw)
