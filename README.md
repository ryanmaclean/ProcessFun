# ProcessFun

## HTTPd Count Shell Script (httpdcount.sh)

*NB: This command should be run via sudo (or as root), otherwise the service restart command could fail.* 

Counts either httpd or apache2 (uncomment the service required) processes and:
 - Prints messages to screen at counts of 1~10, 20~99 and 100+
 - Will restart the service based on the variable if over 100

### Running the Script
1. In order to run the script, download the raw code and pipe it to Bash <pre> curl -L https://raw.githubusercontent.com/ryanmaclean/ProcessFun/master/httpdcount.sh | sudo bash</pre> 

### Resources
If you'd like to make a similar script, or to fork and modify this for your own needs, here are the resources I used:
 - [Check Reply In Range of Numbers] (http://unix.stackexchange.com/questions/118856/check-if-reply-is-in-a-range-of-numbers)
 - [ps Man Page] (http://linux.about.com/od/commands/l/blcmdl1_ps.htm)
 - [grep Man Page] (http://linux.about.com/od/commands/l/blcmdl1_grep.htm)
 - [TLDP on Bash Operators] (http://www.tldp.org/LDP/abs/html/comparison-ops.html)
 - [Large portion of code - Check Process Running] (http://stackoverflow.com/questions/9117507/linux-unix-command-to-determine-if-process-is-running?newreg=f94bc028011b476eae7b6b89bd237934)
