#!/bin/bash

hostname="$(hostname -s)"
ifconfig="$(ip address show)"
osinfo="$(uname -a)"
openports="$(sudo lsof -i -P -n | grep LISTEN)"

echo "{\"hostname\":\""$hostname"\", \"interfaces\":\""$ifconfig"\", \"osinfo\":\""$osinfo"\", \"openports\":\""$openports"\"}"
