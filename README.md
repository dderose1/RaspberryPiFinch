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
The file should then be edited to look like this:
```
# On what interfaces should the DHCP server (dhcpd) serve DHCP requests?
#       Separate multiple interfaces with spaces, e.g. "eth0 eth1".
INTERFACES="wlan0"
```
the interface should be the name of the wifi interface. The next step is to configure the DHCP server. Run the command:

```
sudo nano /etc/dhcp/dhcpd.conf
```
and append the following code to the end of the file

```
subnet 192.168.42.0 netmask 255.255.255.0 {
    range 192.168.42.10 192.168.42.50;
    option broadcast-address 192.168.42.255;
    option routers 192.168.42.1;
    default-lease-time 600;
    max-lease-time 7200;
    option domain-name "local";
    option domain-name-servers 8.8.8.8, 8.8.4.4;
}

```
To change the IP address that will be used to connect to the Finch, the subnet, range, and corresponding IP address in the interfaces file outlined below would have to be changed. A mismatch in any of these fields will cause the connection to fail.

Finally, the `interfaces` file needs to be configured. The config file can be accessed by running:

```
sudo nano /etc/network/interfaces
```

And the file should contain ONLY:

```
iface lo inet loopback

iface eth0 inet dhcp

allow-hotplug wlan0
auto wlan0
iface wlan0 inet static
  address 192.168.42.1
  netmask 255.255.255.0
  wireless-channel 1
  wireless-essid FinchPi1
  wireless-mode ad-hoc
```

This will create the ad hoc network that can be SSH'd into.

### Installing Finch Libraries

The instructions for installing and configuring the official Finch libraries can be found again at [Finch's official website](http://www.finchrobot.com/learning/raspberry-pi). For the sake of efficency, I will not be outlining them here.

### Running programs

Programs can be run over a remote host via `ssh` after being uploaded to the raspberry pi using `scp` or using the pi's gui interface and a flash drive.

The workflow that is currently used for running python scripts is as such 

```
ssh pi@IP_FROM_SETUP
```
Then,
```
cd BBTechSoftwareForPi/FinchPython/
```

and finally running the python script with the `python` command
