import os

class AOpen:

    def __init__(self, file_name, mode = "r", encoding = "utf-8"):
        self.file_name = file_name
        self.encoding = encoding

        mode_list = {
            'r': os.O_RDONLY,
            'w': os.O_WRONLY | os.O_CREAT | os.O_TRUNC,
            'a': os.O_WRONLY | os.O_CREAT | os.O_APPEND,
            'rw': os.O_RDWR | os.O_CREAT,
            'wr': os.O_RDWR | os.O_CREAT | os.O_TRUNC,
            'ra': os.O_RDWR | os.O_APPEND
        }

        # self.mode = mode_list.get(mode, os.O_RDONLY)
        # self.fd = os.open(self.file_name, self.mode)






