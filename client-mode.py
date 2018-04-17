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

# global constants specific to your THETA. Change for your camera.
THETA_ID = 'THETAYL00101082'
THETA_PASSWORD = '00101082'  # default password. may have been changed
THETA_URL = 'http://10.0.0.3:80/osc/'


def get(osc_command):
    url = THETA_URL + osc_command
    resp = requests.get(url, auth=(HTTPDigestAuth(THETA_ID, THETA_PASSWORD)))
    pprint.pprint(resp.json())


def post(osc_command):
    url = THETA_URL + osc_command
    resp = requests.post(url,
                         auth=(HTTPDigestAuth(THETA_ID, THETA_PASSWORD)))
    pprint.pprint(resp.json())

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


get("info")
post("state")
takePicture()