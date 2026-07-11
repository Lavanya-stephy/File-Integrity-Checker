import json

def j_son(data):
    with open("baseline.json","w") as file:
        json.dump(data,file)
