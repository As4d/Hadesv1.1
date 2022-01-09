import pyodbc
import json


class DataAccess:
    def __init__(self):
        self.connectionString = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=tcp:hadesdemo.database.windows.net;PORT=1433;database=hadesdemo;uid=hadesdemoadmin;pwd=*******" # REQURIES PASSWORD AND UID AND DATABASE NAME

    def GetUserCount(self):
        with pyodbc.connect(self.connectionString) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT COUNT(UserId) FROM [User]")
                row = cursor.fetchone()
                return row[0]

    def updateUser(
        self,
        UserId,
        IpAddress,
        TotalFileCount,
        LastScan,
        OperatingSystem,
        NumberOfScans,
    ):
        with pyodbc.connect(self.connectionString) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "UPDATE [User] SET IpAddress = '"
                    + IpAddress
                    + "', TotalFileCount = "
                    + str(TotalFileCount)
                    + ", LastScan = '"
                    + LastScan
                    + "', OperatingSystem = '"
                    + OperatingSystem
                    + "', NumberOfScans = "
                    + str(NumberOfScans)
                    + " WHERE UserId = '"
                    + UserId
                    + "'"
                )

    def createUser(
        self,
        UserId,
        IpAddress,
        TotalFileCount,
        LastScan,
        OperatingSystem,
        NumberOfScans,
    ):
        with pyodbc.connect(self.connectionString) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO [User] (UserId, IpAddress, TotalFileCount, LastScan, OperatingSystem, NumberOfScans) VALUES ('"
                    + UserId
                    + "','"
                    + IpAddress
                    + "',"
                    + str(TotalFileCount)
                    + ",'"
                    + LastScan
                    + "','"
                    + OperatingSystem
                    + "',"
                    + str(NumberOfScans)
                    + ")"
                )

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

    def updateUserTable(self):
        FH = open("User.json")
        data = json.load(FH)
        try:

            self.createUser(
                data["NetworkInfo"]["UserId"],
                data["NetworkInfo"]["ipv4"],
                data["FileCounts"]["total"],
                data["ScanInfo"]["LastScan"],
                data["OS"]["system"],
                data["ScanInfo"]["ScanCount"],
            )

        except:

            self.updateUser(
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
