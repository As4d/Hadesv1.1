import json
import socket
import datetime
import platform
import sqlite3
import uuid
from infector import Infector


class UserInfo:
    def __init__(self):
        self.data = {
            "NetworkInfo": {"ipv4": "", "MachineName": "", "UserId": ""},
            "OS": {"system": "", "version": ""},
            "ScanInfo": {"LastScan": "", "ScanCount": "1"},
            "FileCounts": {},
        }
        self.infector = Infector()

    def updateAllInfo(self):
        self.updateOs()
        self.updateipv4()
        self.updateMachineName()
        self.updateUserId()

    def writeToJson(self):
        self.updateAllInfo()
        self.updateCounts()  # DELETE
        self.updateScanInfo()  # DELETE
        FH = open("User.json", "w")
        FH.write(json.dumps(self.data, indent=4))

    def updateCounts(self):
        fileExtensions = ["txt", "zip", "exe"]
        for extension in fileExtensions:
            self.infector.findFiles(extension)
            self.data["FileCounts"][extension] = len(self.infector.files[extension])
        self.data["FileCounts"]["total"] = self.infector.getTotalNumberOfFiles()

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


class FileHelper:
    def __init__(self):
        self.FH = open("User.json")
        self.UserData = json.load(self.FH)
        self.UserId = None

    def getUserId(self):
        self.UserId = self.UserData["NetworkInfo"]["UserId"]


class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect("test.db")
        self.db = self.connection.cursor()

    def createTable(self):
        self.db.execute(
            """
		CREATE TABLE User (
			UserId UNIQUEIDENTIFIER NOT NULL PRIMARY KEY,
			IpAddress VARCHAR(15) NOT NULL,
			TotalFileCount INT NOT NULL,
			LastScan DATETIME  NOT NULL,
			OperatingSystem VARCHAR(30) NOT NULL,
			NumberOfScans INT NOT NULL
		);
		"""
        )

        self.db.execute(
            """
		CREATE TABLE UserFiles (
			Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			UserId NOT NULL,
			FileType VARCHAR(4) not NULL,
			FileCount INT NOT NULL
		);
		"""
        )

    def updateIntoUser(
        self,
        UserId,
        IpAddress,
        TotalFileCount,
        LastScan,
        OperatingSystem,
        NumberOfScans,
    ):
        self.db.execute(
            "UPDATE User SET IpAddress = ?, TotalFileCount = ?, LastScan = ?, OperatingSystem = ?, NumberOfScans = ? WHERE UserId = ?",
            [
                IpAddress,
                TotalFileCount,
                LastScan,
                OperatingSystem,
                NumberOfScans,
                UserId,
            ],
        )
        self.connection.commit()

    def insertIntoUser(
        self,
        UserId,
        IpAddress,
        TotalFileCount,
        LastScan,
        OperatingSystem,
        NumberOfScans,
    ):
        self.db.execute(
            "INSERT INTO User VALUES (?,?,?,?,?,?)",
            [
                UserId,
                IpAddress,
                TotalFileCount,
                LastScan,
                OperatingSystem,
                NumberOfScans,
            ],
        )
        self.connection.commit()

    def updateIntoUserFiles(self, UserId, FileType, FileCount):
        self.db.execute(
            """UPDATE UserFiles SET FileCount = ? WHERE UserId = ? AND FileType = ?""",
            [FileCount, UserId, FileType],
        )
        self.connection.commit()
        print(self.db.rowcount)
        if self.db.rowcount == 0:
            self.insertIntoUserFiles(self, UserId, FileType, FileCount)
    
    def insertIntoUserFiles(self, UserId, FileType, FileCount):
        self.db.execute(
            "INSERT INTO UserFiles VALUES (NULL,?,?,?)",
            [UserId, FileType, FileCount],
        )
        self.connection.commit()

    def updateUser(self):
        FH = open("User.json")
        data = json.load(FH)
        try:

            self.insertIntoUser(
                data["NetworkInfo"]["UserId"],
                data["NetworkInfo"]["ipv4"],
                data["FileCounts"]["total"],
                data["ScanInfo"]["LastScan"],
                data["OS"]["system"],
                data["ScanInfo"]["ScanCount"],
            )

        except:

            self.updateIntoUser(
                data["NetworkInfo"]["UserId"],
                data["NetworkInfo"]["ipv4"],
                data["FileCounts"]["total"],
                data["ScanInfo"]["LastScan"],
                data["OS"]["system"],
                data["ScanInfo"]["ScanCount"],
            )

    def updateUserFiles(self):
        FH = open("User.json")
        data = json.load(FH)

        for type in data["FileCounts"]:
            if type == "total":
                break
            else:
                self.updateIntoUserFiles(
                    data["NetworkInfo"]["UserId"], type, data["FileCounts"][type]
                )


def main():
    UserInfo().writeToJson()
    DatabaseManager().updateUser()
    DatabaseManager().updateUserFiles()


if __name__ == "__main__":
    main()
