import json
import requests

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
			"19044": "21H2",
		}

	def getWinver(self, buildNumber):
		return self.versions[buildNumber]

	def getWinverFromJson(self):
		FH = open("User.json")
		data = json.load(FH)
		return data["OS"]["version"]

	def getGetVulnerabilitySummary(self):
		apiCall = "https://hadesdemowebapi20220114182325.azurewebsites.net/api/GetVulnerabilitySummary/"
		apiCall += self.getWinverFromJson()
		response = requests.get(apiCall)
		return json.loads(response.content)
	
	def getGetCommonVulnerabilityMetrics(self):
		VulnerabilityMetrics = {}
		apiCall = "https://hadesdemowebapi20220114182325.azurewebsites.net/api/GetVulnerabilityMetric/"
		apiCall += self.getWinverFromJson()
		response = requests.get(apiCall)
		responsedata = json.loads(response.content)
		for data in responsedata:
			VulnerabilityMetrics[data["name"]] = (
				data["value"],
				data["total"]
			)
		return VulnerabilityMetrics