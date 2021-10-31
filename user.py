import json
import socket
import datetime
import platform
from infector import Infector

class UserInfo():

    def __init__(self):
        self.data = {
            'NetworkInfo': {'ipv4': '', 'MachineName': ''},
            'OS' : {'system' : '', 'version' : ''},
            'LastScan': '',
            'FilesCounts' : {'txt' : '', 'zip' : '', 'exe' : ''}
            }

    def updateAllInfo(self):
        self.updateOs()
        self.updateipv4()
        self.updateMachineName()
        
    def writeToJson(self):
        self.updateAllInfo()
        FH = open('User.json', 'w')
        FH.write(json.dumps(self.data, indent=4))
    
    def updateCounts(self):
        self.data['FilesCounts']['txt'] = Infector().getNumberOfTxtFiles()
        self.data['FilesCounts']['exe'] = Infector().getNumberOfExeFiles()
        self.data['FilesCounts']['zip'] = Infector().getNumberOfZipFiles()

    def updateOs(self):
        self.data['OS']['system'] = platform.system()
        self.data['OS']['version'] = platform.version()

    def updateipv4(self):
        self.data['NetworkInfo']['ipv4'] = str(socket.gethostbyname(socket.gethostname()))

    def updateMachineName(self):
        self.data['NetworkInfo']['MachineName'] = str(socket.gethostname())

    def updateLastScan(self):
        self.data['LastScan'] = "{}{}".format(str(datetime.datetime.now())[:10], str(datetime.datetime.now())[10:19])
