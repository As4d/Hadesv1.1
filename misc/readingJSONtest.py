import json

FH = open('User.json')

data = json.load(FH)

for i in data["NetworkInfo"]:
    print(i)