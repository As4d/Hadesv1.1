import json

class CVEHelper:
    def __init__(self):
        self.versions = {
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

    def getWinver(self, buildNumber):
        return self.versions[buildNumber]

    def getNumberOfVulnerablilites(self):
        pass

    def calculatePercentage(self):
        pass    