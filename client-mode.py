#!/usr/bin/python2
"""
Test for THETA V client mode. Your workstation and the THETA V need to be
connected to the same WiFi router or your workstation needs to have two
network interfaces. You can use one Wi-Fi interface as a shared connection
and use it to assign the THETA an IP address.
This test script uses Python modules requests and pprint.
To install requests and pprint

      $ pip install requests
      $ pip install pprint
Once connected with WiFi, use the API here:
https://developers.theta360.com/en/docs/v2.1/api_reference/getting_started.html
The IP address is hardcoded in these tests. To get the IP address, I
am using a separate program that finds the IP of the THETA with NSD
http://lists.theta360.guide/t/developing-theta-client-mode-applications/2450
"""
import requests
from requests.auth import HTTPDigestAuth
import pprint
import sys
import time


# global constants specific to your THETA. Change for your camera.
THETA_ID = 'THETAYL00105377'
THETA_PASSWORD = '00105377'  # default password. may have been changed
THETA_IP = "http://10.42.0.181/"
THETA_URL = THETA_IP + 'osc/'

# this url for testing
testImageUri = "http://10.42.0.181/files/" + \
    "150100525831424d42079d18e0b6c300/100RICOH/R0010194.JPG"

# End of user-defined constants

COMMANDS = ["help",
            "info",
            "state",
            "takePicture",
            "_listPlugins",
            "_setPlugin",
            "listFiles",
            "getImage",
            "imageUrls",
            "downloadTester",
            "takePictureTester"]


def get(osc_command):
    url = THETA_URL + osc_command
    resp = requests.get(url, auth=(HTTPDigestAuth(THETA_ID, THETA_PASSWORD)))
    pprint.pprint(resp.json())


def post(osc_command):
    url = THETA_URL + osc_command
    resp = requests.post(url,
                         auth=(HTTPDigestAuth(THETA_ID, THETA_PASSWORD)))
    pprint.pprint(resp.json())


def helper():
    print("Usage: client-mode.py command")
    print("Available commands:\n")
    for i in range(len(COMMANDS)):
        print(" " + COMMANDS[i])


def runCommand(commandArg):
    if commandArg == "info":
        get("info")
    elif commandArg == "state":
        post("state")
    elif commandArg == "takePicture":
        cameraCommand("takePicture")
    elif commandArg == "_listPlugins":
        cameraCommand("_listPlugins")
    elif commandArg == "listFiles":
        listFiles()
    elif commandArg == "imageUrls":
        imageUrls()
    elif commandArg == "downloadTester":
        downloadTester()
    elif commandArg == "takePictureTester":
        takePictureTester()


def main():
    if len(sys.argv) == 2:
        commandArg = sys.argv[1]
        if commandArg in COMMANDS:
            if commandArg == "help":
                helper()
            elif commandArg == "_setPlugin":
                print("include package name of plug-in to boot")
                print("Example: client-mode.py _setPlugin " +
                      "guide.theta360.long4kvideo")
            elif commandArg == "getImage":
                print("include image URI")
                print("example: client-mode.py getImage " + testImageUri)
            runCommand(commandArg)
        else:
            helper()
    elif len(sys.argv) == 3:
        commandArg = sys.argv[1]
        if commandArg == "_setPlugin":
            setPlugin(sys.argv[2])
        elif commandArg == "getImage":
            getImage(sys.argv[2])

    else:
        helper()


def getImage(url):
    imageName = url.split("/")[6]
    print("saving " + imageName + " to file")
    with open('sampleImg/' + imageName, 'wb') as handle:
        response = requests.get(
                    url,
                    stream=True,
                    auth=(HTTPDigestAuth(THETA_ID, THETA_PASSWORD)))

        if not response.ok:
            print(response)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)


def listFiles():
    url = THETA_URL + 'commands/execute'
    commandString = "camera.listFiles"
    payload = {
                "name": commandString,
                "parameters": {
                    "fileType": "image",
                    "entryCount": 10,
                    "maxThumbSize": 0

                }}
    req = requests.post(url,
                        json=payload,
                        auth=(HTTPDigestAuth(THETA_ID, THETA_PASSWORD)))

    response = req.json()
    print(60 * "=")
    print("client mode listFiles - Testing RICOH THETA API v2.1\n")
    pprint.pprint(response)
    print(str(type(response["results"]["entries"])))


def imageUrls():
    url = THETA_URL + 'commands/execute'
    commandString = "camera.listFiles"
    payload = {
                "name": commandString,
                "parameters": {
                    "fileType": "image",
                    "entryCount": 20,
                    "maxThumbSize": 0

                }}
    req = requests.post(url,
                        json=payload,
                        auth=(HTTPDigestAuth(THETA_ID, THETA_PASSWORD)))

    response = req.json()
    imageEntries = response["results"]["entries"]
    images = []
    for imageEntry in imageEntries:
        print(imageEntry["fileUrl"])
        images.append(imageEntry["fileUrl"])

    return images


def downloadTester():
    print("start download tester")
    images = imageUrls()
    for imageLocation in images:
        getImage(imageLocation)


def takePictureTester():
    print("taking 10 images")
    for pictureNumber in range(10):
        cameraCommand("takePicture")
        print("processing image " + str(pictureNumber + 1))
        print("please wait 5 seconds")
        time.sleep(5)


def cameraCommand(name):
    url = THETA_URL + 'commands/execute'
    commandString = "camera." + name
    payload = {"name": commandString}
    req = requests.post(url,
                        json=payload,
                        auth=(HTTPDigestAuth(THETA_ID, THETA_PASSWORD)))

    response = req.json()
    print(60 * "=")
    print("client mode " + name + " - Testing RICOH THETA API v2.1\n")
    pprint.pprint(response)


def setPlugin(packageName):
    url = THETA_URL + 'commands/execute'
    commandString = "camera._setPlugin"
    payload = {
        "name": commandString,
        "parameters": {
            "packageName": packageName,
            "boot": True
        }}
    req = requests.post(url,
                        json=payload,
                        auth=(HTTPDigestAuth(THETA_ID, THETA_PASSWORD)))

    response = req.json()
    print(60 * "=")
    print("client mode _setPlugin - Testing RICOH THETA API v2.1\n")
    pprint.pprint(response)


main()
