#!/usr/bin/env bash

# get the name of the default printer
PRINTER_NAME=`lpstat -d | sed -e 's/.*: //g'`

if [ -z "$PRINTER_NAME" ]; then
    echo "Failed to find a default printer on the system, aborting."
    exit 1
fi

echo "Using printer with name $PRINTER_NAME"


if [ -z "$1" ]; then
    echo "usage: $0 file-to-print-path"
    exit 2
fi

echo "image attributes..."
file $1
ls -lah $1

lp -E -d $PRINTER_NAME -o media=a6 -o sides=one-sided -o fit-to-page $1
