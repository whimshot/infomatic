#!/usr/bin/env bash

autopep=$(autopep8 -dr .)

if [[ -z $autopep ]]
then
	echo "> PEP8 passed !"
else
	echo "> PEP8 DID NOT pass !"
	echo "$autopep" | colordiff
	exit 1
fi

`nosetests`
if [[ $? != 0 ]]
then
	echo "> Tests DID NOT pass !"
	exit 1
else
	echo "> Tests passed !"
fi

echo "Ready to push !"
exit 0
