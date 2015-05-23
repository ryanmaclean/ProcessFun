#!/bin/bash

#Set the name of the process you want to monitor. 
#Apache2 is commented out, but might be needed depending on your platform
#command="apache2"
command="httpd"

#Count the ammount of processes and store them in the "running" variable
numrunning=`ps cax | grep $command | wc -l`

#Send text to console depending on ammount of running processes

#First case: between 1 and 10
if [ $numrunning >= 1 && $numrunning <= 10 ]; then display="[LOW] Web Server OK!";

#Second case: between 20 and 99
elif [ $numrunning >= 20 && $numrunning < 100 ]; then display="[HIGH] Web Server Working hard!";

#Third case: 100 processes or more
elif [ $numrunning >= 100 ]; then display="[CRITICAL] Web Server under heavy load, restart required";
service $command restart

#Fourth case: If it's less than 1 or between 11 and 20, exit
exit 0;

print $display

fi
