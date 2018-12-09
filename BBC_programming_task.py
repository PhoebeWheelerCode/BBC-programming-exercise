import requests
import re
import json

webAddresses = []
output = []
validURL = re.compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
    r'localhost|' #localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def main():
    print("Enter newline-separated web addresses. When done, enter 'STOP' to stop.")
    while True: #loop until break
        inputText = input()
        if inputText.upper() == "STOP": #if input is break condition
            break #break out of loop
        else: #no newlines, no break
            webAddresses.append(inputText) #append input to list

    for address in webAddresses: #loop through contents of list
        if checkURL(address): #if address is formatted correctly
            jsonValue = getHTTP(address) #Returns response object

            if jsonValue == 'Timeout': #timeout error
                print('Request timed out for URL: ' + address + '\n')
            elif jsonValue == 'ConnectionError': #connection error
                print('Connection error, failed to open URL: ' + address + '\n')
            else: #Successfully retrieved response object
                output.append(getElements(address, jsonValue)) #append json object to output list, containing desired elements
        else: #if address is NOT formatted correctly
            print("Unacceptable URL: " + address + "\n")

    for jsonOutput in output: #print each json object to command line
        print(jsonOutput)

    with open('output.json', 'w') as f:
        f.write("[\n")
        for jsonOutput in output:
            f.write(jsonOutput + '\n')
        f.write("]")

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

def getElements(url, jsonVal):
    values = {}
    values.update(
                {"Url": url,
                "Status_code": jsonVal.status_code,
                "Content_length": len(jsonVal.raw.read()),
                "Date": jsonVal.headers['Date']
                }
                )
    return json.dumps(values, indent=4)

if __name__ == "__main__":
    main()
