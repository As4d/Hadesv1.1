import json

class CVEHelper:
    def __init__(self):
        self.__versions = {
            "10240": "1507",
            "10586": "1511",
            "14393": "1607",
            "15063": "1703",
            "16299": "1709",
            "17134": "1803",
            "17763": "1809",
            "18362": "1903",
            "18363": "1909",
            "19041": "2004",
            "19042": "20H2",
            "19043": "21H1",
            "19044": "21H2"
        }
        self._winver = ""

    def __getBuildNumber(self):
        FH = open("User.json")
        data = json.load(FH)
        return data["OS"]["BuildNumber"]

    def getWinver(self):
        return self.__winver

    def _setWinver(self):
        self.__winver = self.__versions[self.__getBuildNumber()]

    def getNumberOfVulnerablilites(self):
        pass

    def calculatePercentage(self):
        pass    