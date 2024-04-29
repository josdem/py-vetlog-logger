import os
import logging

class Logger:
    def __init__(self, path):
        self.path = path
        self.prepare_file()
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.INFO)
        self.create_handler()
    
    def prepare_file(self):
        if not os.path.exists(self.path):
            open(self.path, 'a')

    def create_handler(self):
        self.formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
        file_handler = logging.FileHandler(self.path)
        self.logger.addHandler(file_handler)
        file_handler.setFormatter(self.formatter)

    def get_logger(self):
        return self.logger        