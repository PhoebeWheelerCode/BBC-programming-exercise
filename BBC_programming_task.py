import urllib.request

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

for address in webAddresses: #loop through contents of list
    print(address) # temp - for now, print element of list
