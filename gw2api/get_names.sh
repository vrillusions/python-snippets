#!/bin/bash -e
#
# Downloads the json files containing the id-name mappings for:
#   - worlds
#   - maps
#   - events
#
# Only need to run this on initial checkout just to find your values

# Usage: log "What to log"
log () {
    printf "%b\n" "$(date +"%Y-%m-%dT%H:%M:%S%z") $*"
}

# set script_dir to location this script is running in
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

log "Downloading list of worlds"
curl -s https://api.guildwars2.com/v1/world_names.json >${SCRIPT_DIR}/world_names.json

log "Downloading list of maps"
curl -s https://api.guildwars2.com/v1/map_names.json >${SCRIPT_DIR}/map_names.json

log "Downloading list of events"
curl -s https://api.guildwars2.com/v1/event_names.json >${SCRIPT_DIR}/event_names.json

log "Finished"

exit 0

