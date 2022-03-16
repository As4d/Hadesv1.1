from winreg import *

aKey = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)

print(r"*** Reading from %s ***" % aKey)

aKey = OpenKey(aReg, aKey)
for i in range(1024):
    try:
        asubkey_name = EnumKey(aKey, i)
        asubkey = OpenKey(aKey, asubkey_name)
        val = QueryValueEx(asubkey, "DisplayName")
        print(val)
    except EnvironmentError:
        break