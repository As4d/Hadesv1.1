from cvehelper import CVEHelper

class Score(CVEHelper):
    def __init__(self, scannerObj, fileHelperObj):
        self.scanner = scannerObj
        self.filehelper = fileHelperObj
        self.colour = {
            (0, 19): "Green",
            (20, 39): "Lime",
            (40, 59): "Yellow",
            (60, 79): "Orange",
            (80, 100): "Red"
        }
        self.totalvulnerabilities = 0
        self.metricScores = {}

    def calculateColour(self, int):
        for range in self.colour:
            if int >= range[0] and int <= range[1]:
                return self.colour[range]

    def getGetCommonVulnerabilityMetrics(self):
        return super().getGetCommonVulnerabilityMetrics()
    
    def getGetVulnerabilitySummary(self):
        return super().getGetVulnerabilitySummary()
    
    def getTotalvulnerabilities(self):
        return self.totalvulnerabilities
    
    def setTotalvulnerabilities(self, int):
        self.totalvulnerabilities = int

    def calculateMetricScores(self):
        self.metricScores = {}
        self.setTotalvulnerabilities(self.getGetVulnerabilitySummary()[0]["noOfVulnerabilities"])
        arr = self.getGetCommonVulnerabilityMetrics()
        for i in arr:
            percentage = int((arr[i][1] / self.getTotalvulnerabilities()) * 100 )
            colour = self.calculateColour(percentage)
            self.metricScores[i] = (arr[i][0], colour, percentage)
        return self.metricScores
    
    def getMetricValue(self, metric):
        return self.metricScores[metric][0]
    
    def getMetricColour(self, metric):
        return self.metricScores[metric][1]
    
    def getMetricScore(self, metric):
        return self.metricScores[metric][2]
    