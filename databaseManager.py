import sqlite3

class DatabaseManager():
    
    def __init__(self):
        self.connection = sqlite3.connect('test.db')
        self.db = self.connection.cursor()

    def createTable(self):
        self.db.execute('''CREATE TABLE User (
    UserId INT NOT NULL AUTO_INCREMENT,
    IpAddress VARCHAR(15) NOT NULL,
    TotalFileCount INT NOT NULL,
    LastScan DATETIME  NOT NULL,
  	OperatingSystem VARCHAR(30) NOT NULL,
  	NumberOfScans INT NOT NULL,
    PRIMARY KEY(UserId)
);

CREATE TABLE UserFiles (
    Id INT NOT NULL AUTO_INCREMENT,
    UserId INT NOT NULL,
    FileType VARCHAR(4) not NULL,
    FileCount INT NOT NULL,
    PRIMARY KEY(Id)
);
        ''')