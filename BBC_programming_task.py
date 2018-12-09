import urllib.request
import requests
import re
import json

webAddresses = []

print("Enter newline-separated web addresses. When done, enter 'STOP' to stop.")
while True: #loop until break
    inputText = input()
    if inputText.upper() == "STOP": #if input is break condition
        break #break out of loop
    elif "\n" in inputText: #if input string contains newlines
        splitInput = inputText.split("\n") #split by newlines
        for address in splitInput: #loop through split addresses
            webAddresses.append(address) #append to list
    else: #no newlines, no break
        webAddresses.append(inputText) #append input to list

validURL = re.compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
    r'localhost|' #localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def checkURL(userInputURL):
    if re.match(validURL, userInputURL) == None: # if none, there is no match
        return False
    else:
        return True

def getHTTP(userInputURL):
    try:
        return requests.get(userInputURL, stream=True, timeout=10, headers={'accept': 'application/json'})
    except requests.exceptions.Timeout:
        return 'Timeout'
    except requests.exceptions.ConnectionError:
        return 'ConnectionError'

def getElements(url, json):
    values = {}
    values.update(
                {"Url": url,
                "Status_code": json.status_code,
                "Content_length": len(json.raw.read()),
                "Date": json.headers['Date']
                }
                )
    return values

for address in webAddresses: #loop through contents of list
    #print(address) # temp - for now, print element of list
    if checkURL(address):
        jsonValue = getHTTP(address)

        if jsonValue == 'Timeout':
            print('Timed out request for URL: ' + address + '\n')
        elif jsonValue == 'ConnectionError':
            print('Failed to open URL: ' + address + '\n')
        else:
            print(getElements(address, jsonValue))
            print()
    else:
        print("Unacceptable URL: " + address + "\n")
