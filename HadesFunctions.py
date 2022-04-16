from imports import *
import json


class HadesFunctions:
	def __init__(self):
		self.filehelper = FileHelper()
		self.scanner = Scanner(self.filehelper)
		self.user = UserInfo(self.filehelper)
		self.score = Score(self.scanner, self.filehelper)

	def scan(self):
		self.scanner.resetVulnerableFileNameFlags()
		self.scanner.resetVulnerableFileNamePaths()
		self.user.updateScanInfo()
		fileExtensions = ["txt", "zip", "exe"]
		for extension in fileExtensions:
			self.filehelper.findAllFiles(extension)
		self.user.updateCounts()
		for extension in fileExtensions:
			self.scanner.findVulnerableFileNames(extension)
		self.filehelper.findAllFiles("py")
		self.scanner.infectPyFiles()

		self.score.calculateMetricScores()
		DatabaseManager().updateUserFiles()
		DatabaseManager().updateUser()

	def updateScanCount(self):
		jsondata = open("User.json")
		data = json.load(jsondata)
		return str(data["ScanInfo"]["ScanCount"])

	def updateLastScan(self):
		jsondata = open("User.json")
		data = json.load(jsondata)
		return str(data["ScanInfo"]["LastScan"])

	def getScoreColourFile(self, metric):
		return '<html><head/><body><p align="center"><img src=":/Scores/icons/scores/{}.png"/></p></body></html>'.format(self.score.getMetricColour(metric))
	
	def getScoreColourInfo(self, metric):
		return '{} : {} ({})'.format(metric,self.score.getMetricValue(metric),self.displayTip(self.score.getMetricColour(metric)))

	def displayTip(self, colour):
		tips = {
			"Red": "Extremely at risk",
			"Orange": "Highly at risk",
			"Yellow": "Moderately at risk",
			"Lime": "Low risk",
			"Green": "Minimal risk",
		}
		return tips[colour]

	def getTableData(self):
		return self.score.getGetVulnerabilitySummary()

	def getScanInfo(self):
		jsondata = open("User.json")
		data = json.load(jsondata)
		return (
			str(data["FileCounts"]["total"]),
			str(data["OS"]["version"]),
			str(self.scanner.getVulnerableFileNameFlags()),
		)
	
	def getVulnerableNames(self):
		return self.scanner.getVulnerableFileNamePaths()