from dataStructures import Queue
import os
import re


class Infector:
    def __init__(self):
        self.qtxt = Queue()
        self.qzip = Queue()
        self.qexe = Queue()
        self.files = [self.qexe, self.qzip, self.qtxt]

    def findAllFiles(self):
        self.findExeFiles()
        self.findTxtFiles()
        self.findZipFiles()

    def findTxtFiles(self):
        for files in os.walk(r"C:\Users\asadk\Documents\TEST"):  #
            for file in files[2]:
                if (file.split(".")[-1]) == "txt":
                    # print("File found: " + files[0] + "\\" + file)
                    self.qtxt.enqueue(files[0] + "\\" + file)

    def findZipFiles(self):
        for files in os.walk(r"C:\Users\asadk\Documents\TEST"):  #
            for file in files[2]:
                if (file.split(".")[-1]) == "zip":
                    # print("File found: " + files[0] + "\\" + file)
                    self.qzip.enqueue(files[0] + "\\" + file)

    def findExeFiles(self):
        for files in os.walk(r"C:\Users\asadk\Documents\TEST"):  #
            for file in files[2]:
                if (file.split(".")[-1]) == "exe":
                    # print("File found: " + files[0] + "\\" + file)
                    self.qexe.enqueue(files[0] + "\\" + file)

    def getNumberOfTxtFiles(self):
        return self.qtxt.getLenQueue()

    def getNumberOfExeFiles(self):
        return self.qexe.getLenQueue()

    def getNumberOfZipFiles(self):
        return self.qzip.getLenQueue()

    def getTotalNumberOfFiles(self):
        return (
            self.qzip.getLenQueue() + self.qexe.getLenQueue() + self.qtxt.getLenQueue()
        )

    def searchVulnerableFileNames(self):
        temp = 0
        vulnerablestrings = [
            "password",
            "account",
            "statement",
            "bank",
            "passport",
            "drivers liscense",
            "pin",
        ]
        for q in self.files:
            for file in q.queue:
                if str(file.split("\\")[-1].split(".")[0]) in vulnerablestrings:
                    print(
                        "Vulnerable File name:",
                        "'{}'".format(file.split("\\")[-1].split(".")[0]),
                    )
                    temp += 1
                    self.findVulnerablitiesInTxt(file)
        return temp

    def findVulnerablitiesInTxt(self, file):
        FH = [x.strip() for x in open(file, "r").readlines()]
        vulnerablestrings = [
            "password",
            "account",
            "statement",
            "bank",
            "passport",
            "drivers liscense",
            "pin",
        ]
        for sentence in FH:
            for string in vulnerablestrings:
                x = re.findall("(?i)({}):*s*".format(string), sentence)
                if x != []:
                    print(x)
