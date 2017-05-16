# RaspberryPiFinch

## Raspberry Pi Controlled Finch Robot Documentation
## By Dylan Derose

### About

The goal of this project was to make the Finch robot by BirdBrain technologies run untethered by attaching a raspberry pi standalone computer to the robot, and have it run the programs required to power the robot. The only major requirements are the Finch Raspberry pi libraries found at: [Finch's Official Website](http://www.finchrobot.com/learning/raspberry-pi) and the `isc-dhcp-server`package.

### Raspberry Pi Setup

The instructions for installing the Raspbian operating system can be found [here](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md) and is required for the system to run properly. You should then run the commands `sudo apt-get update` and `sudo apt-get install isc-dhcp-server`. Once installed, The network settings on the Pi must be configured.

### Network Configuration

The first package to be configured is the `isc-dhcp-server`, whose config file can be accessed by running the command:
```
sudo nano /etc/default/isc-dhcp-server
```
