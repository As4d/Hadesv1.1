from user import UserInfo
from databasemanager import DatabaseManager

def main():
    UserInfo().writeToJson()
    DatabaseManager().updateUser()
    DatabaseManager().updateUserFiles()

if __name__ == "__main__":
    main()