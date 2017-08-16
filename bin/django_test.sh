#!/bin/bash

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
NOCOLOR='\033[0m'

echo "DJANGO MODULE ${DJANGO_SETTINGS_MODULE}"

# Runing PEP8 recursive in all .py files
#N_ERRORS=`find . -name \*.py -exec pep8 --exclude=migrations {} + | wc -l`
N_ERRORS=$(pep8 . | wc -l)

if [ ${N_ERRORS} -eq 0 ]; then

	echo -e "${GREEN}Success${NOCOLOR}: PEP8 not found errors"

else
    echo -e "${RED}ERROR${NOCOLOR}: PEP8 encountered ${N_ERRORS} errors."
    pep8 .
    exit 1
fi

