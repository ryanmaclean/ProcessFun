#!/bin/bash

#Set the name of the process you want to monitor. 
#Apache2 is commented out, but might be needed depending on your platform 
#E.g.: Debian family, used for testing

#command="apache2"
command="httpd"

#Initialize restart variable to false as the command could be run more than once in a session
restart=false

#Count the ammount of processes and store them in the "numrunning" variable
numrunning=`ps cax | grep $command | wc -l`

#Send text to console depending on ammount of running processes

#First case: between 1 and 10
if [ $numrunning -ge 1 -a $numrunning -lt 10 ]; then 
	display="[LOW] Web Server OK!";

#elif [ $numrunning -gt 10 -a $numrunning -le 20 ]; then 
#	display="[MED] Web Server Normal";

#Second case: between 20 and 100
elif [ $numrunning -gt 20 -a $numrunning -le 100 ]; then 
	display="[HIGH] Web Server Working hard!";

#Third case: 100 processes or more
elif [ $numrunning -gt 100 ]; then 
	display="[CRITICAL] Web Server under heavy load, restart required";
	restart=true

else
#Exit gracefully if between 10 and 20
exit 0;
fi

#Restart service if required
if $restart; then
	restarttext="Restarting process"
	service $command restart
fi

#Display the text if set
echo $display
