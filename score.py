class Score:
    def __init__(self):
        self.score = 100
        self.colour = {
            (0, 24): "Red",
            (25, 49): "Orange",
            (50, 74): "Yellow",
            (75, 100): "Green",
        }

    def CalculateCoulour(self):
        for range in self.colour:
            if self.score >= range[0] and self.score <= range[1]:
                return self.colour[range]

    def CalculateAcessMetric(self):
        pass

    def CalculateIntegrityMetric(self):
        pass

    def CalculateConfidentialityMetric(self):
        pass

    def GetVulnerableFileNameFlags(self):
        pass

    def GetVulnerableTextInFileFlags(self):
        pass

    def GetPythonFilesAccessed(self):
        pass