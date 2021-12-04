import sqlite3
from user import UserInfo

class DatabaseManager():

	def __init__(self):
		self.connection = sqlite3.connect('test.db')
		self.db = self.connection.cursor()

	def CREATE_TABLE(self):
		self.db.execute('''
		CREATE TABLE User (
			UserId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			IpAddress VARCHAR(15) NOT NULL,
			TotalFileCount INT NOT NULL,
			LastScan DATETIME  NOT NULL,
			OperatingSystem VARCHAR(30) NOT NULL,
			NumberOfScans INT NOT NULL
		);
		''')

		self.db.execute('''
		CREATE TABLE UserFiles (
			Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			UserId INT NOT NULL,
			FileType VARCHAR(4) not NULL,
			FileCount INT NOT NULL
		);
		''')
	
	def checkUserId(self, Ip):
		if self.db.execute("SELECT EXISTS(SELECT UserId FROM User WHERE UserId = ?)", [Ip]).fetchone() == (1,):
			return True
	
	def INSERT_INTO_User(self,
						 IpAddress,
						 TotalFileCount,
						 LastScan,
						 OperatingSystem,
						 NumberOfScans):
		self.db.execute('INSERT INTO User VALUES (NULL,?,?,?,?,?)', [IpAddress,
																	 TotalFileCount,
																	 LastScan,
																	 OperatingSystem,
																	 NumberOfScans])
		self.connection.commit()
	
	def INSERT_INTO_UserFiles(self,
						 	  UserId,
						      TotalFileCount,
						      FileType,
						      FileCount):
		self.db.execute('INSERT INTO UserFiles VALUES (NULL,?,?,?,?)', [UserId,
																	 TotalFileCount,
																	 FileType,
																	 FileCount])
		self.connection.commit()

	def SELECT_User(self):
		print("==================== DATABASE TABLE User ====================")
		for row in self.db.execute('SELECT * FROM User'):
			print(row)

	def SELECT_UserFiles(self):
		print("==================== DATABASE TABLE UserFiles ====================")
		for row in self.db.execute('SELECT * FROM UserFiles'):
			print(row)
	
	def updateUser(self):
		try:
			FH = open('User.json')
			data = json.load(FH)
			self.INSERT_INTO_User(
				  data['NetworkInfo']['ipv4'],
				  data['FilesCounts']['total'],
				  data['ScanInfo']['LastScan'],
				  data['OS']['system'],
				  data['ScanInfo']['ScanCount'])
		except:
			UserInfo().writeToJson()
			FH = open('User.json')
			data = json.load(FH)
			self.INSERT_INTO_User(
				  data['NetworkInfo']['ipv4'],
				  data['FilesCounts']['total'],
				  data['ScanInfo']['LastScan'],
				  data['OS']['system'],
				  data['ScanInfo']['ScanCount'])
	
	def updateUserFiles(self):
		try:
			FH = open('User.json')
			data = json.load(FH)
			print(
				  data['NetworkInfo']['ipv4'],
				  data['FilesCounts']['total'],
				  data['FilesCounts']['LastScan'],
				  data['FilesCounts']['system'])
		except:
			UserInfo().writeToJson()
			FH = open('User.json')
			data = json.load(FH)
			print(
				  data['NetworkInfo']['ipv4'],
				  data['FilesCounts']['total'],
				  data['FilesCounts']['LastScan'],
				  data['FilesCounts']['system'])