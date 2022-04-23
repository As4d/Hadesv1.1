import os
import pathlib

class FileHelper:

    def __init__(self): 
        self.files = {}
        self.fileExtensions = ["txt", "zip", "exe"]

    def setFileExtensions(self, arr):
        self.fileExtensions = arr
    
    def getFileExtensions(self):
        return self.fileExtensions

    def findAllFiles(self, extension):
        filesFound = []
        for files in os.walk(pathlib.Path.home()):
            for file in files[2]:
                if file.split(".")[-1] == extension.lower():
                    filesFound.append(files[0] + "\\" + file)
        self.files[extension] = filesFound
    
    def getTotalNumberOfFiles(self):
        total = 0
        for key in self.fileExtensions:
            total += len(self.files[key])
        self.files['total'] = total
        return self.files['total']
    
    def getTotalNumberOfFilesExt(self, extension):
        return len(self.files[extension])
    
    def getFilesList(self, extension):
        return self.files[extension]
