import sqlite3
import json

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
        if self.db.rowcount == 0:
            self.insertIntoUserFiles(UserId, FileType, FileCount)
    
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