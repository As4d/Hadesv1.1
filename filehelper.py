import os
import pathlib

class FileHelper:

    def __init__(self):
        self.files = {}

    def findAllFiles(self, extension):
        filesFound = []
        for files in os.walk(pathlib.Path.home()):  # pathlib.Path.home() / r"C:\Users\asadk\Documents\TEST"
            for file in files[2]:
                if file.split(".")[-1] == extension.lower():
                    #print("File found: " + files[0] + "\\" + file + "\n")
                    filesFound.append(files[0] + "\\" + file)
        self.files[extension] = filesFound
        return filesFound

    def findFilesInDir(self, extension, dir):
        files = {}
        filesFound = []
        for files in os.walk(dir):  # pathlib.Path.home()
            for file in files[2]:
                if file.split(".")[-1] == extension.lower():
                    #print("File found: " + files[0] + "\\" + file + "\n")
                    filesFound.append(files[0] + "\\" + file)
                    files[extension.lower()] = filesFound
        return files
    
    def getTotalNumberOfFiles(self):
        total = 0
        for key in self.files:
            total += len(self.files[key])
        self.files['total'] = str(total)
        return total
    
    def getTotalNumberOfFilesExt(self, extension):
        return len(self.files[extension])