import os

class FileHelper:

    def findAllFiles(self, extension):
        filesFound = []
        for files in os.walk(r"C:\Users\asadk\Documents\TEST"):  # pathlib.Path.home()
            for file in files[2]:
                if file.split(".")[-1] == extension.lower():
                    #print("File found: " + files[0] + "\\" + file + "\n")
                    filesFound.append(files[0] + "\\" + file)
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