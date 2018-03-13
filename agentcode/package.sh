#!/bin/bash

## Temp fix. Need to replace with complied bin for specific platform
gcc ./caller/caller.c

resourceInfo="$(sudo bash ./scripts/agent.sh)"

registryIp="$(awk '/^ip/{print $3}' config.conf)"
registryPort="$(awk '/^port/{print $3}' config.conf)"

echo "$(registryIp)"
echo "$(registryPort)"

./a.out "$(registryIp)" "$(registryPort)" 3000 POST /registerResource "$(resourceInfo)" "Content-Type: application/json"
