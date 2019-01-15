#!/usr/bin/python2
"""
Test for THETA V client mode. Your workstation and the THETA V need to be
connected to the same WiFi router.
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
import shutil
from PIL import Image
from io import BytesIO

# global constants specific to your THETA. Change for your camera.
THETA_ID = 'THETAYL00105377'
THETA_PASSWORD = '00105377'  # default password. may have been changed
THETA_IP = "http://10.42.0.181/"
THETA_URL = THETA_IP + 'osc/'

# End of user-defined constants

COMMANDS = ["help",
            "info",
            "state",
            "takePicture",
            "_listPlugins",
            "_setPlugin",
            "listFiles",
            "getImage"]


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
    elif commandArg == "getImage":
        getImage()


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
            runCommand(commandArg)
        else:
            helper()
    elif len(sys.argv) == 3:
        commandArg = sys.argv[1]
        if commandArg == "_setPlugin":
            setPlugin(sys.argv[2])

    else:
        helper()


def getImage():
    with open('sampleImg/pic1.jpg', 'wb') as handle:
        url = "http://10.42.0.181/files/150100525831424d42079d18e0b6c300/100RICOH/R0010194.JPG"
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
                    "maxThumbSize": 640

                }}
    req = requests.post(url,
                        json=payload,
                        auth=(HTTPDigestAuth(THETA_ID, THETA_PASSWORD)))

    response = req.json()
    print(60 * "=")
    print("client mode listFiles - Testing RICOH THETA API v2.1\n")
    pprint.pprint(response)


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
