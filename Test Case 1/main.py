# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import base64
import csv
import random

def initializeNames(lineNum):
    with open('credentials.csv', 'w', newline='') as file:
        sheetdata = []
        namesFile = open("names.txt", "r")
        writer = csv.writer(file)
        writer.writerow(["username", "password", "errormessage"])
        for i in range(lineNum):
            username = "o" + namesFile.readline().rstrip()
            sample_string_bytes = username.encode("ascii")
            base64_bytes = base64.b64encode(sample_string_bytes)
            password = base64_bytes.decode("ascii")
            newrow = [username, password, ""]
            sheetdata.append(newrow)
        writer.writerows(sheetdata)
        counterFile = open("counter.txt", "w")
        counterFile.write(str(lineNum))



def create_users(lineNum):
    # Use a breakpoint in the code line below to debug your script.
    numCaseOne = lineNum * 0.05
    numCaseTwo = lineNum * 0.1
    numCaseThree = lineNum * 0.1
    numCaseFour = lineNum * 0.25
    numCaseFive = lineNum * 0.5
    print(str(numCaseTwo))
    counterFile = open("counter.txt", "r")
    namesTraversed = int(counterFile.read())
    if namesTraversed == 0:
        initializeNames(lineNum)
    else:
        spots = [None] * lineNum
        counter = 0
        while counter < int(numCaseOne):
            spot = random.randint(0,lineNum-1)
            if spots[spot] is None:
                spots[spot] = 1
                counter+=1

        counter = 0
        while counter < int(numCaseTwo):
            spot = random.randint(0,lineNum-1)
            if spots[spot] is None:
                spots[spot] = 2
                counter+=1

        counter = 0
        while counter < int(numCaseThree):
            spot = random.randint(0,lineNum-1)
            if spots[spot] is None:
                spots[spot] = 3
                counter+=1
        counter = 0

        while counter < int(numCaseFour):
            spot = random.randint(0,lineNum-1)
            if spots[spot] is None:
                spots[spot] = 4
                counter+=1
        counter = 0

        with open('credentials.csv', 'w', newline='') as correctFile, open('logincredentials.csv', 'w', newline='') as loginCredFile:
            signupWriter = csv.writer(correctFile)
            loginWriter = csv.writer(loginCredFile)
            signupWriter.writerow(["username", "password", "statuscode", "errormessage"])
            loginWriter.writerow(["loginusername", "loginpassword", "loginstatuscode", "loginerrormessage"])
            namesFile = open("names.txt", "r")
            lines = namesFile.readlines()
            signupSheetData = []
            loginSheetData = []
            for i in range(lineNum):
                if spots[i] == 1:
                    randNum = random.randint(0, namesTraversed)
                    username = "o" + lines[randNum].rstrip()
                    sample_string_bytes = username.encode("ascii")
                    base64_bytes = base64.b64encode(sample_string_bytes)
                    password = base64_bytes.decode("ascii")
                    signUpRow = [username, password, "200","This user already exist"]
                    loginRow = ["", password, "500", "500"]
                    signupSheetData.append(signUpRow)
                    loginSheetData.append(loginRow)

                elif spots[i] == 2:
                    randNum = random.randint(0, namesTraversed)
                    username = "o" + lines[randNum].rstrip()
                    sample_string_bytes = username.encode("ascii")
                    base64_bytes = base64.b64encode(sample_string_bytes)
                    password = base64_bytes.decode("ascii")
                    signUpRow = [username, password, "200", "This user already exist"]
                    loginRow = [username, password, "200", "Auth_token"]
                    signupSheetData.append(signUpRow)
                    loginSheetData.append(loginRow)

                elif spots[i] == 3:
                    signinUsername = "o" + lines[0].rstrip()
                    sample_string_bytes = signinUsername.encode("ascii")
                    base64_bytes = base64.b64encode(sample_string_bytes)
                    signinPassword = base64_bytes.decode("ascii")

                    loginUsername = "o" + lines[namesTraversed+counter+1].rstrip()
                    sample_string_bytes = loginUsername.encode("ascii")
                    base64_bytes = base64.b64encode(sample_string_bytes)
                    loginPassword = base64_bytes.decode("ascii")

                    signinRow = [signinUsername, signinPassword, "200", "This user already exist"]
                    loginRow = [loginUsername, loginPassword, "200", "User does not exist"]
                    print(str(i) + str(spots[i]))
                    signupSheetData.append(signinRow)
                    loginSheetData.append(loginRow)

                elif spots[i] == 4:
                    randNum = random.randint(0, namesTraversed)
                    signinUsername = "o" + lines[0].rstrip()
                    sample_string_bytes = signinUsername.encode("ascii")
                    base64_bytes = base64.b64encode(sample_string_bytes)
                    signinPassword = base64_bytes.decode("ascii")

                    loginUsername = "o" + lines[namesTraversed+randNum].rstrip()
                    sample_string_bytes = loginUsername.encode("ascii")
                    base64_bytes = base64.b64encode(sample_string_bytes)
                    loginPassword = "q" + base64_bytes.decode("ascii")

                    signinRow = [signinUsername, signinPassword, "200", "This user already exist"]
                    loginRow = [loginUsername, loginPassword, "200", "User does not exist"]
                    print(str(i) + str(spots[i]))
                    signupSheetData.append(signinRow)
                    loginSheetData.append(loginRow)
                else:
                    signinUsername = "o" + lines[namesTraversed+counter].rstrip()
                    sample_string_bytes = signinUsername.encode("ascii")
                    base64_bytes = base64.b64encode(sample_string_bytes)
                    signinPassword = base64_bytes.decode("ascii")

                    loginUsername = "o" + lines[namesTraversed + counter].rstrip()
                    sample_string_bytes = loginUsername.encode("ascii")
                    base64_bytes = base64.b64encode(sample_string_bytes)
                    loginPassword = base64_bytes.decode("ascii")

                    signinRow = [signinUsername, signinPassword, "200", ""]
                    loginRow = [loginUsername, loginPassword, "200", "Auth_tok"]
                    signupSheetData.append(signinRow)
                    loginSheetData.append(loginRow)
                    counter+=1
            signupWriter.writerows(signupSheetData)
            loginWriter.writerows(loginSheetData)
        counterFile = open("counter.txt", "r")
        namesTraversed = int(counterFile.readline())
        counterFile = open("counter.txt", "w")
        counterFile.write(str(int(namesTraversed + numCaseFive)))
        print(spots)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_users(250)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
