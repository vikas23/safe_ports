#!/bin/bash

## Resource Info
hostname="$(hostname -s)"
osinfo="$(uname -a)"
cpuinfo="$(cat /proc/cpuinfo)"

## Network and Ports Info
ifconfig="$(ifconfig -a)"
openports="$(sudo netstat -tulpn)"


echo "{\"hostname\":\""$hostname"\", \"interfaces\":\""$ifconfig"\", \"osinfo\":\""$osinfo"\", \"openports\":\""$openports"\", \"cpuinfo\":\""$cpuinfo"\"}"
