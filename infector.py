from dataStructures import Queue
import os

class Infector():

    def __init__(self):
        self.qtxt = Queue()
        self.qzip = Queue()
        self.qexe = Queue()
        self.findAllFiles()

    def findAllFiles(self):
        self.findExeFiles()
        self.findTxtFiles()
        self.findZipFiles()

    def findTxtFiles(self):
        for files in os.walk(r"C:\Users\asadk\Documents\TEST"): #
            for file in files[2]:
                if (file.split(".")[-1]) == "txt":
                    #print("File found: " + files[0] + "\\" + file)
                    self.qtxt.enqueue(files[0] + "\\" + file)
    
    def findZipFiles(self):
        for files in os.walk(r"C:\Users\asadk\Documents\TEST"): #
            for file in files[2]:
                if (file.split(".")[-1]) == "zip":
                    #print("File found: " + files[0] + "\\" + file)
                    self.qzip.enqueue(files[0] + "\\" + file)
    
    def findExeFiles(self):
        for files in os.walk(r"C:\Users\asadk\Documents\TEST"): #
            for file in files[2]:
                if (file.split(".")[-1]) == "exe":
                    #print("File found: " + files[0] + "\\" + file)
                    self.qexe.enqueue(files[0] + "\\" + file)
            
    def getNumberOfTxtFiles(self):
        return self.qtxt.getLenQueue()
    
    def getNumberOfExeFiles(self):
        return self.qexe.getLenQueue()
    
    def getNumberOfZipFiles(self):
        return self.qzip.getLenQueue()

    def getTotalNumberOfFiles(self):
        count = 0
        for files in os.walk(r"C:\Users\asadk\Documents\TEST"):
            for file in files[2]:
                count += 1
        return count
    
    def searchVulnerableFileNames(self):
        files = [self.qtxt, self.qzip, self.qexe]
        lines = [x[:-1] for x in open("VulnerableFilesNames.txt", "r").readlines()]
        for q in files:
            for file in q.queue:
                if str(file.split("\\")[-1].split(".")[0]) in lines:
                    print("Vulnerable File name:", "'{}'".format(file.split("\\")[-1].split(".")[0]), "wtf man")

root = Infector()
root.searchVulnerableFileNames()