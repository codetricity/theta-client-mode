#!/usr/bin/python2
"""
Test for THETA V client mode. Your workstation and the THETA V need to be
connected to the same WiFi or Ethernet router.
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

# global constants specific to your THETA. Change for your camera.
# THETA_ID = 'THETAYL00105377' # THETA S
# THETA_PASSWORD = '00105377'  # default password. may have been changed
THETA_ID = 'THETAYN10010104'  # THETA Z1
THETA_PASSWORD = '10010104'
THETA_URL = 'http://192.168.2.101/osc/'


def get(osc_command):
    url = THETA_URL + osc_command
    resp = requests.get(url, auth=(HTTPDigestAuth(THETA_ID, THETA_PASSWORD)))
    pprint.pprint(resp.json())


def post(osc_command):
    url = THETA_URL + osc_command
    resp = requests.post(url,
                         auth=(HTTPDigestAuth(THETA_ID, THETA_PASSWORD)))
    pprint.pprint(resp.json())


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


def setOptions():
    url = THETA_URL + 'commands/execute'
    payload = {"name": "camera.setOptions",
               "parameters": {
                   "options": {
                       "exposureProgram": 1,
                       "shutterSpeed": 0.002,
                       "_autoBracket": {
                           "_bracketNumber": 3,
                           "_bracketParameters": [
                               {
                                   "aperture": 2.1,
                                   "_colorTemperature": 5000,
                                   "exposureCompensation": 0,
                                   "exposureProgram": 1,
                                   "iso": 400,
                                   "shutterSpeed": 0.004,
                                   "whiteBalance": "auto"
                               },
                               {
                                   "aperture": 2.1,
                                   "_colorTemperature": 3000,
                                   "exposureCompensation": 0,
                                   "exposureProgram": 1,
                                   "iso": 800,
                                   "shutterSpeed": 0.004,
                                   "whiteBalance": "auto"
                               },
                               {
                                   "aperture": 2.1,
                                   "_colorTemperature": 4000,
                                   "exposureCompensation": 0,
                                   "exposureProgram": 1,
                                   "iso": 1000,
                                   "shutterSpeed": 0.004,
                                   "whiteBalance": "auto"
                               },
                           ],
                       }

                   }
               }
               }

    req = requests.post(
        url,
        json=payload,
        auth=(HTTPDigestAuth(THETA_ID, THETA_PASSWORD)))

    response = req.json()
    print(60 * "=")
    print("client mode setOptions - Testing RICOH THETA API v2.1\n")
    pprint.pprint(response)


def getOptions():
    url = THETA_URL + 'commands/execute'
    payload = {
        "name": "camera.getOptions",
        "parameters": {
            "optionNames": [
                "exposureProgram",
                "_autoBracket"
            ]
        }
    }

    req = requests.post(
        url,
        json=payload,
        auth=(HTTPDigestAuth(THETA_ID, THETA_PASSWORD)))

    response = req.json()
    print(60 * "=")
    print("client mode getOptions - Testing RICOH THETA API v2.1\n")
    pprint.pprint(response)


get("info")
setOptions()
getOptions()
# post("state")
# takePicture()
