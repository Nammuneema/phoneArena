import json

def getName ():
    #----Getting URL of the selected Phone----
    with open('../Data/online/data2.json') as f:
        details = json.loads(f.read())
        return details

#print(getURL())