from user import UserInfo
from databasemanager import DatabaseManager

def main():
    user = UserInfo()
    user.updateScanInfo()
    user.updateCounts()
    DatabaseManager().updateUser()
    DatabaseManager().updateUserFiles()

if __name__ == "__main__":
    main()