import os

class Entry:
    def __init__(self, path):
        self.path = path

    def name(self):
        return os.path.basename(self.path)
    
    def isdir(self):
        return os.path.isdir(self.path)
    
    def islink(self):
        return os.path.islink(self.path)
    
    def size(self):
        return os.path.getsize(self.path)
    
    def modified(self):
        return os.path.getmtime(self.path)