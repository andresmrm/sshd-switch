# SSHD Switch

Small app to turn on/off SSHD. Tested only on CyanogenMod.

![Interface example with a menu displaying the sshd status and start and stop buttons.](https://rawgit.com/andresmrm/sshd-switch/master/screen.png)

Basically it's an interface with buttons to execute `start-ssh` and `killall sshd` as root.
So the app will need **root** access and these commands must be acceptable to start and stop sshd.

This app is built in Python using [python-for-android](https://github.com/kivy/python-for-android). Using a webview that uses the Flask web framework. So the app itself is a browser viewing a local instance of a Flask server.

## Install

First configure your SSHD. For CyanogenMod follow [this guide](https://wiki.cyanogenmod.org/w/Doc:_sshd).

Then install the apk and run!

## Use

Click "start" to start SSHD (wait 3 seconds for status to update).
Click "stop" to stop SSHD (running SSH connections will continue, not sure why).
Click status (yes or no) to refresh the SSHD status (can be usefull...).

## Run Dependencies

Dependencies needed to run this app:

- netcat (to check SSHD status)
- start-ssh
- killall
- echo
- bash
- su

## Build

First install python-for-android.
Then run `build.sh`.
Then `deploy-run.sh` to deploy to a connected device and start the app.
