import json
import datetime
import platform
import uuid
import requests
import os
from cvehelper import CVEHelper


class UserInfo():
    def __init__(self, obj):
        self.data = {
            "NetworkInfo": {"ipv4": "", "UserId": ""},
            "OS": {"system": "", "version": ""},
            "ScanInfo": {"LastScan": "", "ScanCount": "0"},
            "FileCounts": {},
        }
        self.fileHelper = obj
        self.cvehelper = CVEHelper()
        self.FILEPATH = os.path.expanduser('~') + "\\HadesFiles\\User.json"

    def updateAllInfo(self):
        self.updateOs()
        self.updateipv4()
        self.updateUserId()

    def writeToJson(self):
        self.updateAllInfo()
        try:

            FH = open(self.FILEPATH, "w")
            FH.write(json.dumps(self.data, indent=4))

        except:
            os.mkdir(os.path.expanduser('~') + "\HadesFiles")
            FH = open(self.FILEPATH, "w")
            FH.write(json.dumps(self.data, indent=4))

    def updateCounts(self):
        fileExtensions = self.fileHelper.getFileExtensions()
        for extension in fileExtensions:
            self.data["FileCounts"][extension] = self.fileHelper.getTotalNumberOfFilesExt(extension)
        self.data["FileCounts"]["total"] = self.fileHelper.getTotalNumberOfFiles()
        self.writeToJson()

    def updateOs(self):
        self.data["OS"]["system"] = platform.system()
        self.data["OS"]["BuildNumber"] = platform.version().split('.')[2]
        self.data["OS"]["version"] = self.cvehelper.getWinver(platform.version().split('.')[2])

    def updateipv4(self):
        try:

            response = requests.get("http://ipinfo.io/json").json()
            self.data["NetworkInfo"]["ipv4"] = response["ip"]

        except (requests.ConnectionError, requests.Timeout) as exception:
            print(exception.response)
            return False

    def updateScanInfo(self):
        self.data["ScanInfo"]["LastScan"] = str(datetime.datetime.now()).split(".")[0]
        try:
            FH = open(os.path.expanduser('~') + "\\HadesFiles\\User.json")
            data = json.load(FH)
            self.data["ScanInfo"]["ScanCount"] = str(
                int(data["ScanInfo"]["ScanCount"]) + 1
            )
        except:
            pass
        self.writeToJson()

    def updateUserId(self):
        try:
            FH = open(self.FILEPATH)
            data = json.load(FH)
            if data["NetworkInfo"]["UserId"] == "":
                self.data["NetworkInfo"]["UserId"] = str(uuid.uuid4())
            else:
                self.data["NetworkInfo"]["UserId"] = data["NetworkInfo"]["UserId"]
        except:
            self.data["NetworkInfo"]["UserId"] = str(uuid.uuid4())
    
    def getUserFilePath(self):
        return self.FILEPATH