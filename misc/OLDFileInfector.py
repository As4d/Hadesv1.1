import os
import datetime
from ds import Queue

class FileInfector():

    def __init__(self):
        self.logs = open("Logs.txt", "a")
        self.filesCount = open("Filescount.txt", "r")
        self.infectedTxtCount = 0
        self.infectedDocxCount = 0
        self.fileFirstCount = {"txt" : str(self.filesCount.readline()).split("\n")[0], "docx" : str(self.filesCount.readline()).split("\n")[0]}
        self.filesCount.close()
        

    def updateFilesCount(self):
        FileIn = open("Filescount.txt", "w")
        FileIn.write(str(int(self.fileFirstCount["txt"]) + self.infectedTxtCount)   + "\n")
        FileIn.write(str(int(self.fileFirstCount["docx"]) + self.infectedDocxCount) + "\n")
        FileIn.close()

    def updateLogs(self, fileLocation):
        self.logs.write("{}{} {}\n".format(str(datetime.datetime.now())[:10], str(datetime.datetime.now())[10:19], fileLocation))

    def infectTxtFiles(self):
        
        for files in os.walk(r"N:\test"): # BECAREFUL NOT THE CHANGE THE FILE PATH OTHERWISE YOULL MESS UP THE FILES (need to make recursion func to loop through destinations)
            for file in files[2]:
                if (file.split(".")[-1]) == "txt":
                    print("_" * len(files[0] + file))
                    print(files[0] + "\\" + file)
                    self.updateLogs(files[0] + "\\" + file)
                    FileIn = open(files[0] + "\\" + file, "a")
                    FileIn.write("INFECTED")
                    self.infectedTxtCount += 1
                    print("Has been infected") 
                    print("_" * len(files[0] + "\\" + file))
                    
        FileIn.close()
    
    def getNumberOfFiles(self):
        count = 0
        for files in os.walk(r"C:\Users\asadk\Documents"):
            for file in files[2]:
                count += 1
        return count
