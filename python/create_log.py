
class Logger:
    def __init__(self, path):
        self.path = path
        file = open(path, "a")
        file.close()