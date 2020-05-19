#!/bin/bash

IP_ADDRESS="192.168.2.101"
BASE_URL="http://$IP_ADDRESS/"
# THETA_ID="THETAYL00126042"
# PASSWORD="00126042"

THETA_ID="THETAYL00105377"
PASSWORD="00105377"
GET_INFO="${BASE_URL}osc/info"

# curl --digest --user "${THETA_ID}:${PASSWORD}"  $GET_INFO


# curl --digest --user "THETAYL00105377:00105377" -X GET http://192.168.2.101/osc/info

# curl --digest --user "THETAYL00105377:00105377" -H "Content-Type:application/json" -X POST http://192.168.2.101/osc/state

curl -d '{"name":"camera.takePicture"}' --digest --user "THETAYL00105377:00105377" -H "Content-Type:application/json; charset=utf-8;" -X POST http://192.168.2.101/osc/commands/execute
