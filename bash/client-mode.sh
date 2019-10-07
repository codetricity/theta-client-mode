#!/bin/bash

IP_ADDRESS="192.168.2.102"
BASE_URL="http://$IP_ADDRESS/"
# THETA_ID="THETAYL00126042"
# PASSWORD="00126042"

THETA_ID="THETAYL00105377"
PASSWORD="00105377"
GET_INFO="${BASE_URL}osc/info"

# curl -D - --digest -u "${THETA_ID}:${PASSWORD}"  $GET_INFO

curl -D - -H "Content-Type:application/json" --digest -u "THETAYL00126042:00126042" -X GET "http://192.168.2.102/osc/info"