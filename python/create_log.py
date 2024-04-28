def create_log():
    file = open("vetlog.log", "a")
    file.write("Now the file has more content!")
    file.close()
    return file