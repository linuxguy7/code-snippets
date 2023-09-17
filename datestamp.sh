#!/bin/bash

DATE_STAMP="$(date +%d%m%y)_ $(($(date +%s) - $(date -d "$(date '+%B %d, %Y')" +%s)))"  



# Can also source this file to get `datestamp` function (returns datestamp for current time)
datestamp () {
    echo "$(date +%d-%m-%y)_$(($(date +%s) - $(date -d "$(date '+%B %d, %Y')" +%s)))"
}

return 
