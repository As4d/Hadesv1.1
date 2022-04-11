import json
import requests
from datetime import datetime


class DatabaseManager:
    def updateIntoUser(
        self, UserId, IpAddress, TotalFileCount, OperatingSystem, NumberOfScans
    ):

        jsonData = {
            "UserId": UserId,
            "IpAddress": IpAddress,
            "LastScan": datetime.now().isoformat(),
            "NoOfScans": NumberOfScans,
            "OperatingSystem": OperatingSystem,
            "TotalFileCount": TotalFileCount,
        }
        try:
            response = requests.put(
                "https://hadesdemowebapi20220114182325.azurewebsites.net/api/updateuser",
                json=jsonData,
            )

            if response.text == "0":
                self.insertIntoUser(
                    UserId, IpAddress, TotalFileCount, OperatingSystem, NumberOfScans
                )

        except (requests.ConnectionError, requests.Timeout) as exception:
            print("Failed to connect")
            return False

    def insertIntoUser(
        self, UserId, IpAddress, TotalFileCount, OperatingSystem, NumberOfScans
    ):

        jsonData = {
            "UserId": UserId,
            "IpAddress": IpAddress,
            "LastScan": datetime.now().isoformat(),
            "NoOfScans": NumberOfScans,
            "OperatingSystem": OperatingSystem,
            "TotalFileCount": TotalFileCount,
        }
        response = requests.post(
            "https://hadesdemowebapi20220114182325.azurewebsites.net/api/createuser",
            json=jsonData,
        )

        if response.text == "false":
            pass

    def updateIntoUserFiles(self, UserId, FileType, FileCount):
        jsonData = {"UserId": UserId, "FileType": FileType, "FileCount": FileCount}
        response = requests.put(
            "https://hadesdemowebapi20220114182325.azurewebsites.net/api/updateuserfiles",
            json=jsonData,
        )
        if response == "0":
            self.insertIntoUserFiles()

    def insertIntoUserFiles(self, UserId, FileType, FileCount):
        jsonData = {"UserId": UserId, "FileType": FileType, "FileCount": FileCount}
        response = requests.post(
            "https://hadesdemowebapi20220114182325.azurewebsites.net/api/createuserfiles",
            json=jsonData,
        )

    def updateUser(self):
        FH = open("User.json")
        data = json.load(FH)
        self.updateIntoUser(
            str(data["NetworkInfo"]["UserId"]),
            str(data["NetworkInfo"]["ipv4"]),
            str(data["FileCounts"]["total"]),
            str(data["OS"]["version"]),
            str(data["ScanInfo"]["ScanCount"]),
        )

    def updateUserFiles(self):
        FH = open("User.json")
        data = json.load(FH)

        for type in data["FileCounts"]:
            if type == "total":
                break
            else:
                self.updateIntoUserFiles(
                    str(data["NetworkInfo"]["UserId"]),
                    str(type),
                    str(data["FileCounts"][type]),
                )
