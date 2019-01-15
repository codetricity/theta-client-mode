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

# global constants specific to your THETA. Change for your camera.
THETA_ID = 'THETAYL00105377'
THETA_PASSWORD = '00105377'  # default password. may have been changed
THETA_URL = 'http://192.168.2.100/osc/'

COMMANDS = ["info", "state", "takePicture"]


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


def main():
    if len(sys.argv) == 2:
        commandArg = sys.argv[1]
        if commandArg in COMMANDS:
            runCommand(commandArg)
        else:
            helper()
    else:
        helper()
    # print(str(sys.argv))


# def post(osc_command):
#     url = THETA_URL + osc_command
#     resp = requests.post(url)
#     print(resp)


def takePicture():
    url = THETA_URL + 'commands/execute'
    payload = {"name": "camera.takePicture"}
    req = requests.post(url,
                        json=payload,
                        auth=(HTTPDigestAuth(THETA_ID, THETA_PASSWORD)))

    response = req.json()
    print(60 * "=")
    print("client mode takePicture - Testing RICOH THETA API v2.1\n")
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


main()
# get("info")
# post("state")
# takePicture()
