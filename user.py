import json
import socket
import datetime
import platform
import sqlite3
import uuid
from infector import Infector
from infector import FileHelper


class UserInfo:
    def __init__(self):
        self.data = {
            "NetworkInfo": {"ipv4": "", "MachineName": "", "UserId": ""},
            "OS": {"system": "", "version": ""},
            "ScanInfo": {"LastScan": "", "ScanCount": "1"},
            "FileCounts": {},
        }
        self.infector = Infector(FileHelper())

    def updateAllInfo(self):
        self.updateOs()
        self.updateipv4()
        self.updateMachineName()
        self.updateUserId()

    def writeToJson(self):
        self.updateAllInfo()
        FH = open("User.json", "w")
        FH.write(json.dumps(self.data, indent=4))

    def updateCounts(self):
        fileExtensions = ["txt", "zip", "exe"]
        for extension in fileExtensions:
            self.infector.findFiles(extension)
            self.data["FileCounts"][extension] = len(self.infector.files[extension])
        self.data["FileCounts"]["total"] = self.infector.getTotalNumberOfFiles()
        self.writeToJson()

    def updateOs(self):
        self.data["OS"]["system"] = platform.system()
        self.data["OS"]["version"] = platform.version()

    def updateipv4(self):
        self.data["NetworkInfo"]["ipv4"] = str(
            socket.gethostbyname(socket.gethostname())
        )

    def updateMachineName(self):
        self.data["NetworkInfo"]["MachineName"] = str(socket.gethostname())

    def updateScanInfo(self):
        self.data["ScanInfo"]["LastScan"] = str(datetime.datetime.now()).split(".")[0]
        try:
            FH = open("User.json")
            data = json.load(FH)
            self.data["ScanInfo"]["ScanCount"] = str(
                int(data["ScanInfo"]["ScanCount"]) + 1
            )
        except:
            pass
        self.writeToJson()

    def updateUserId(self):
        try:
            FH = open("User.json")
            data = json.load(FH)
            if data["NetworkInfo"]["UserId"] == "":
                self.data["NetworkInfo"]["UserId"] = str(uuid.uuid4())
            else:
                self.data["NetworkInfo"]["UserId"] = data["NetworkInfo"]["UserId"]
        except:
            self.data["NetworkInfo"]["UserId"] = str(uuid.uuid4())