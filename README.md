# THETA V Client Mode Tests

Use Digest Authentication.

Your THETA V and your workstation must be connected to the same
WiFi router or Ethernet switch/hub. You can also connect your THETA to the Wi-Fi of your
laptop or workstation if you share the Wi-Fi connection.  
The THETA V WiFi LED should be solid green, not blue.  If you are assigning the THETA an IP
address with DHCP, people have reported success with both the internal router DHCP (such as an
inexpensive D-Link home router) or a DHCP server running on a Linux server/workstation.  See this
[thread](https://community.theta360.guide/t/how-to-connect-theta-v-with-ethernet/3298?u=codetricity) for more information on using Ethernet.

Thanks these people for Ethernet testing:

* [Kev091190](https://community.theta360.guide/u/Kev091190) - first person to figure out that THETA V can be powered by USG OTG 'Y' connector. Also contributed extensive performance tests.
* [nasos333](https://community.theta360.guide/u/nasos333) - successfully tested Linux DHCP server

## Find IP Address

To find the IP address of the THETA V:

    $ python3 find-theta.py

## Test Client Mode

1. change the IP address in `client-mode.py` to the IP address of your THETA V.
2. change the THETA_ID and THETA_PASSWORD constants to your specific camera.

Run test:

    $ python client-mode.py info

or if you are using Linux and your PATH is set to the current directory:

    $ client-mode.py info

### Current commands

* help
* info
* state
* takePicture - take a single picture
* _listPlugins - list installed plug-ins
* _setPlugin - set active plug-in to boot. Requires package name on command line
* listFiles - print last 10 files, including metadata
* imageUrls - print last 20 image file URLs
* getImage - download image and save to file. Requires URL on command line
* imageUrls - print last 20 image URLs

### Testing Commands

* downloadTester - download last 20 images
* takePictureTester - take 10 images
