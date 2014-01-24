#!/bin/bash

# comment out the following line to disable messages
#VERBOSE=1

if [ $VERBOSE ]; then
  echo -e "Rename script started at:\t$(date)";
  echo -e "Parameter \$1 is:\t\t$1"
  echo -e "current directory is:\t\t$(pwd)"
  echo -e "move command is:\t\tmv -T -f \"$1\" '/var/www/poza3.jpg'"
fi

# move the temporary file to a given filename
mv -T -f "$1" '/var/www/poza3.jpg'

RES=$?
if [ $VERBOSE ]; then
  echo -e "move command returned:\t\t$RES"
fi
