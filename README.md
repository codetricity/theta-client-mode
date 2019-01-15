# THETA V Client Mode Tests

Use Digest Authentication.

Your THETA V and your workstation must be connected to the same
WiFi router.  The THETA V WiFi LED should be solid green, not blue.

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

Current commands
    "help",
    "info",
    "state",
    "takePicture",
    "_listPlugins",
    "_setPlugin"