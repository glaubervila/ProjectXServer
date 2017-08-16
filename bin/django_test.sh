#!/bin/bash

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
NOCOLOR='\033[0m'

echo "Running PEP8 checks"
N_ERRORS=$(pep8 . | wc -l)

if [ ${N_ERRORS} -eq 0 ]; then

	echo -e "${GREEN}Success${NOCOLOR}: PEP8 not found errors"

else
    echo -e "${RED}ERROR${NOCOLOR}: PEP8 encountered ${N_ERRORS} errors."
    # Running PEP8 again to display errors
    pep8 .
    # Mark build proccess with error
    exit 1
fi


echo "Running Tests With Coverage"

# If DJANGO_SETTING_MODULE run tests using this conf else run with settings.test
if [ ${DJANGO_SETTINGS_MODULE} ];then

    echo "Using ${DJANGO_SETTINGS_MODULE}"

    coverage run manage.py test --settings=${DJANGO_SETTINGS_MODULE}

else
    coverage run manage.py test --settings=server.settings.test

fi

echo "Running Coveralls"
coveralls