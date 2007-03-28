import os
import time

class Entry:
    def __init__(self, path):
        self.path = path
        self.base = '/Users/tgl/'

    def name(self):
        return os.path.basename(self.path)
    
    def basename(self):
        return os.path.basename(self.path)

    def dirname(self):
        return os.path.dirname(self.path)
    
    def path_without_base(self):
        return self.path.replace(self.base, '', 1)
        
    def path_with_dashes(self):
        return os.path.basename(self.path)
 
    def path_encrypted(self):
        return os.path.basename(self.path)
    
    def isdir(self):
        return os.path.isdir(self.path)
    
    def islink(self):
        return os.path.islink(self.path)
    
    def size(self):
        filesize = os.path.getsize(self.path)
        if filesize < 1000:
            size = str(filesize) + "&nbsp;B"
        elif filesize >= 1000:
            size = str(filesize/1000) + "&nbsp;kB"
        elif filesize >= 10000:
            size = str(filesize/10000) + "&nbsp;MB"
        return size
        
    def modified(self):
        dateTime = os.path.getmtime(self.path)
        date = time.strftime("%Y-%m-%d %H:%M", time.gmtime(dateTime))
        return date